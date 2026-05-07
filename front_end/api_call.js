class DjangoCall {
    // constructor(cat_type) {
        // this.cat_type = cat_type;
    // }
    async api_request() {
        try {
            const response = await fetch("http://127.0.0.1:8000/soulsborne/");
            if(!response.ok) {
                throw new Error(`Response status: ${response.status}`);
            }
            const result = await response.json();
            // console.log(result);
            // populate(result);
            return result;
        }
        catch (error) {
            console.error(error.message);
        }
    }
    async loadJSON(fieldValue, cat_type) {
        const apiArray = await this.api_request();
        // insert way to categorize JSON by category type...pyromancy for default for now
        const loreTable = document.getElementById('lore-table');
        loreTable.innerHTML = "";
        // **** A/N: Sort out issue of incrementing / extracting API based on
        // category ****
        let incr = 1;
        for(let i = 0; i < apiArray.length; i++) {
            // important note: extracing entity id can be done by either
            // OBJECT[index].id or OBJECT[index]["id"]
            const temp_type = apiArray[i]["category_type"];
            const row = `
            <tr>
                <td><img src="../Images/DS/${temp_type}/${temp_type}_${incr}.png"></td>
                <td>${apiArray[i]["item_name"]}</td>
                <td>${apiArray[i]["item_use"]}</td>
                <td>${apiArray[i]["item_availability"]}</td>
                <td>${apiArray[i]["item_description"]}</td>
                <td>${apiArray[i]["category_type"]}</td>


                <td>
                    <textarea id="comments" name="comments" rows="5" cols="35">Enter your theories, ideas, beliefs, etc as you see fit.</textarea>
                    <button type="button" class="commenting" data-id="${apiArray[i].id}">Post</button>
                    <div></div>
                </td>
                <td>
                    <textarea id="tags" name="tags" rows="1" cols="32">A tagging system to sort ideas.</textarea>
                    <button type="button" class="tagging" data-id="${apiArray[i].id}">Add</button>
                    <div></div>
                </td>

            </tr>`;

            // sorts by parameter rather than specific
            // actually, why does this even work? 
            // switching the order of the conditions breaks everything
            // ref: apiArray[i]["category_type"] == fieldValue

            if(fieldValue == apiArray[i][cat_type]) {
                loreTable.innerHTML += row;
                incr++;
            }
            else { continue; }
        }
        this.addListeners();
        // this.doesAttributeExist();
    }

    addListeners() {
        // is called before the fact to avoid spamming API
        let btnTaggingClass = document.querySelectorAll(".tagging");
        let results = this.doesAttributeExist([...btnTaggingClass], "tags");
        
        // runs through PSQL DB to see if there are any existing tags
        // while simultaneously attaching eventListeners to buttons
        results.then((dict) => {
            btnTaggingClass.forEach((button) => {
                button.addEventListener("click", () => {
                    // grabs value relative to the button that was clicked.
                    // using "tags" id would grab the first element instead
                    let tagValue = button.previousElementSibling.value;  
                    // console.log(tagValue);
                    this.handleAPIForm("tags", button.dataset.id, tagValue);
                });
              
                // console.log(dict[button.dataset.id]);
                let div = document.querySelector(`.tagging[data-id="${button.dataset.id}"]`);
                
                // evaluates if an entity has any tags or not before populating associated div element
                if(dict[button.dataset.id].length > 0) {
                    // for(let i = 0; i < dict[button.dataset.id].length; i++) {
                        div.nextElementSibling.innerHTML = "Tags: " + dict[button.dataset.id].join(", ");
                    // }
                } 
                else { div.nextElementSibling.innerHTML = "No tags"; }
            });
        });        

        let btnCommentingClass = document.querySelectorAll(".commenting");
        results = this.doesAttributeExist([...btnCommentingClass], "comments");
        results.then((dict) => {
            btnCommentingClass.forEach((button) => {
                button.addEventListener("click", () => {
                    let commentValue = button.previousElementSibling.value;
                    // console.log(commentValue);
                    this.handleAPIForm("comments", button.dataset.id, commentValue);
                });
                //
                let div = document.querySelector(`.commenting[data-id="${button.dataset.id}"]`);
                    
                // evaluates if an entity has any comments or not before populating associated div element
                if(dict[button.dataset.id].length > 0) {
                    // for(let i = 0; i < dict[button.dataset.id].length; i++) {
                        div.nextElementSibling.innerHTML = "Comments: " + dict[button.dataset.id].join(", ");
                    // }
                } 
                else { div.nextElementSibling.innerHTML = "No comments"; }
            });
        });
    }
    

    async doesAttributeExist(btnClassArray, btnType) {
        try {
            let results = {};
            switch(btnType) {
                case "tags":
                    // iterates & retrieves tags associated with entity id
                    let response = await fetch(
                        `http://127.0.0.1:8000/soulsborne/tagsofentities`
                    );
                    let entityTagArray = await response.json();
        
                    // let results = {};
                    
                    for(let outer = 0; outer < btnClassArray.length; outer++) {
                        let tags = [];
                        for(let inner = 0; inner < entityTagArray.length; inner++) {
                            if(btnClassArray[outer].dataset.id == entityTagArray[inner]["entity"]) {
                                if(entityTagArray[inner]["tag"] != null){
                                    let response2 = await fetch(
                                        `http://127.0.0.1:8000/soulsborne/tags/?id=${entityTagArray[inner]["tag"]}`
                                    );
                                    let tagArray = await response2.json();
        
                                    for(let index = 0; index < tagArray.length; index++) {
                                        tags.push(tagArray[index]["tag"]);
                                    }
                                } // add else continue?
                            }
                        }
                        // console.log(`${btnClassArray[outer].dataset.id} has ${counter} matches in the database!`);
                        results[btnClassArray[outer].dataset.id] = tags;
                    }
                    break;
                case "comments":
                    let commentResponse = await fetch(
                        `http://127.0.0.1:8000/soulsborne/interpretationofentities`
                    );
                    let entityCommentArray = await commentResponse.json();
        
                    // let results = {};
                    for(let outer = 0; outer < btnClassArray.length; outer++) {
                        let comments = [];
                        for(let inner = 0; inner < entityCommentArray.length; inner++) {
                            if(btnClassArray[outer].dataset.id == entityCommentArray[inner]["entity"]) {
                                if(entityCommentArray[inner]["interpret"] != null){
                                    let response2 = await fetch(
                                        `http://127.0.0.1:8000/soulsborne/interpretations/?id=${entityCommentArray[inner]["interpret"]}`
                                    );
                                    let commentArray = await response2.json();
        
                                    for(let index = 0; index < commentArray.length; index++) {
                                        comments.push(commentArray[index]["comments"]);
                                    }
                                } // add else continue?
                            }
                        }
                        // console.log(`${btnClassArray[outer].dataset.id} has ${counter} matches in the database!`);
                        results[btnClassArray[outer].dataset.id] = comments;
                    }
                    break;
            }
            console.log(results);
            return results;
        }
        catch(error) {
            console.error("Error has been caught: ");
            console.error(error.message);
        }
    }


    async handleAPIForm(fieldType, entity_id, fieldValue) {
        console.log("fieldType:", fieldType);
        console.log("entity_id:", entity_id);
        try {
            let response = null;
            
            switch(fieldType) {
                case "comments":
                    response = await fetch("http://127.0.0.1:8000/soulsborne/interpretations/", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({
                            comments: fieldValue
                        })
                    });

                    let getCommentID = await response.json();
                    let commDerResponse = await fetch("http://127.0.0.1:8000/soulsborne/interpretationofentities/", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({
                            entity: entity_id,
                            interpret: getCommentID.id
                        })
                    });
                    break;

                case "tags":
                    response = await fetch("http://127.0.0.1:8000/soulsborne/tags/", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({
                            tag: fieldValue
                        })
                    });

                    let tagDerResponse = await response.json();
                    await fetch("http://127.0.0.1:8000/soulsborne/tagsofentities/", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({
                            entity: entity_id,
                            tag: tagDerResponse.id
                        })
                    });
                    break;
            }
            
            if(!response.ok) {
                throw new Error(`Response status: ${response.status}`);
            }
            console.log("the truth was reached!");
        }
        catch (error) {
            console.error("the truth was never reached: ");
            console.error(error.message);
        }
    }
    

    async updatePage() {
        const sortSelect = document.getElementById("sort").value;
        const bySelect = document.getElementById("by").value;
        console.log(bySelect);
        
        switch(sortSelect) {
            case "category":
                const lowercasedString = bySelect.toLowerCase();
                await this.loadJSON(lowercasedString, "category_type");
                break;
            case "location":
                await this.loadJSON(bySelect, "item_availability");
                break;
            case "tags":
                await this.loadJSON(bySelect);
                break;
            case "alpha":
                await this.loadJSON(bySelect);
                break;
            case "rev_alpha":
                await this.loadJSON(bySelect);
                break;
        }
    }


    async extractField(selectedOption) {
        console.log(selectedOption);
        const reqData = await this.api_request();
        const tempArray = [];
        for(let i = 0; i < reqData.length; i++) {
            tempArray.push(reqData[i][selectedOption]);
        }
        const uniqueFieldSet = new Set(tempArray);
        const setArray = Array.from(uniqueFieldSet);
        const sortByVal = document.getElementById("by");
        sortByVal.innerHTML = "";
        for(let i = 0; i < setArray.length; i++) {
            let capitalize = setArray[i].charAt(0).toUpperCase() + setArray[i].slice(1);
            sortByVal.innerHTML += `
                <option value="${setArray[i]}">${capitalize}</option>
            `;
        }
    }
}