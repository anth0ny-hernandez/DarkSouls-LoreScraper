from darksouls_class import DarkSouls
import requests
import json

# quick tip: remember to change "category_type" and subdirectory/filename names

# ds1 = DarkSouls("http://darksouls.wikidot.com/sorceries", "class", "wiki-content-table")
ds2 = DarkSouls("http://darksouls.wikidot.com/sorceries", "class", "wiki-content-table")
# ds3 = DarkSouls("http://darksouls.wikidot.com/covenants", "class", "wiki-content-table")

# print(ds1.url)
# ds1.get_all_urls("class", "wiki-content-table")
results = ds2.run()
formatted = []
for item in results:
    formatted.append(
        {
            "url": item[0],
            "item_icon": item[1],
            "item_name": item[2],
            "item_use": item[3],
            "item_availability": item[4],
            "item_description": item[5],
            "category_type": "sorcery"
        }
    )

# self-note: 'with' automatically closes open files (and more...)
with open('./scraped_data.json', 'w') as f:
    json.dump(formatted, f, indent=2)

# script to POST the data to the API localhost as soon as it's consolidated
with open('scraped_data.json') as f:
    items = json.load(f)
    
i = 1
for item in items:
    response = requests.post(
        'http://127.0.0.1:8000/soulsborne/',
        json=item
    )
    print(f"{item['item_name']}: {response.status_code}")
    # section to request data at the url and locally download them
    # file names are at your discretion
    img_url = requests.get(item["item_icon"]).content
    
    with open(f'Images/DS/sorcery/sorcery_{i}.png', 'wb') as g:
        g.write(img_url)
    i+=1
