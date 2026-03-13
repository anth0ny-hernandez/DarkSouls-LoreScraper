from darksouls_class import DarkSouls
import requests
import json

# ds1 = DarkSouls("http://darksouls.wikidot.com/consumables", "class", "wiki-content-table")
ds2 = DarkSouls("http://darksouls.wikidot.com/consumables", "class", "wiki-content-table")
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
            "item_description": item[5]
        }
    )

# self-note: 'with' automatically closes open files (and more...)
with open('./scraped_data.json', 'w') as f:
    json.dump(formatted, f, indent=2)

# script to POST the data to the API localhost as soon as it's consolidated
with open('scraped_data.json') as f:
    items = json.load(f)
    
for item in items:
    response = requests.post(
        'http://127.0.0.1:8000/soulsborne/',
        json=item
    )
    print(f"{item['item_name']}: {response.status_code}")