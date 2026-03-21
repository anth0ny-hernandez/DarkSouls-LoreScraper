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
            const temp_type = apiArray[i]["category_type"]; // just for directory navigation
            const row = `
            <tr>
                <td><img src="../Images/DS/${temp_type}/${temp_type}_${incr}.png"></td>
                <td>${apiArray[i]["item_name"]}</td>
                <td>${apiArray[i]["item_use"]}</td>
                <td>${apiArray[i]["item_availability"]}</td>
                <td>${apiArray[i]["item_description"]}</td>
                <td>${apiArray[i]["category_type"]}</td>
                <td>
                    <input type="button" formmethod="post" 
                    type="submit" value="Comment" onclick="">
                </td>
                <td>
                    <input type="button" formmethod="post" 
                    type="submit" value="Add" onclick="">
                </td>
            </tr>`;
            // if(apiArray[i]["category_type"] == fieldValue) { 
            //     loreTable.innerHTML += row;
            //     incr++;
            // }
            // else { continue; }

            // sorts by parameter rather than specific
            // actually, why does this even work? 
            // switching the order of the conditions breaks everything
            if(fieldValue == apiArray[i][cat_type]) {
                loreTable.innerHTML += row;
                incr++;
            }
            else { continue; }
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