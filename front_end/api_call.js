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
    // apiArray = await api_request();
    async loadJSON(cat_type) {
        const apiArray = await this.api_request();
        // insert way to categorize JSON by category type...pyromancy for default for now
        const loreTable = document.getElementById("lore-table");
        loreTable.innerHTML = "";
        // **** A/N: Sort out issue of incrementing / extracting API based on
        // category ****
        let incr = 1;
        // let cat_type; for now pyro will be the placeholder
        // let cat_type = "pyromancy"
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
            if(apiArray[i]["category_type"] == cat_type) { 
                loreTable.innerHTML += row;
                incr++;
            }
            else { continue; }
        }
    }

    
    async updatePage() {
        const sortSelect = document.getElementById("sort").value;
        const bySelect = document.getElementById("by").value;
        const lowercasedString = bySelect.toLowerCase();
        
        switch(sortSelect) {
            case "category":
                await this.loadJSON(lowercasedString);
        }
    }


    async extractField() {
        const filterArray = await this.api_request();
        const category_array = [];
        for(let i = 0; i < filterArray.length; i++) {
            category_array.push(filterArray[i]["category_type"]);
        }
        const uniqueCat = new Set(category_array);
        const amogus = Array.from(uniqueCat);
        const sortByVal = document.getElementById("by");

        for(let i = 0; i < amogus.length; i++) {
            let capitalize = amogus[i].charAt(0).toUpperCase() + amogus[i].slice(1);
            sortByVal.innerHTML += `
                <option value="${amogus[i]}">${capitalize}</option>
            `;
        }
    }
}