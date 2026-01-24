import requests
from bs4 import BeautifulSoup

#url = "http://darksouls.wikidot.com/moonlight-set"
# url = "http://darksouls.wikidot.com/crimson-set"
url = "http://darksouls.wikidot.com/adventurer-s-set"
headers = {
    "User-Agent": "DS1 LoreScraper (small, amateur personal project)"
}
page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="page-content")
tables = results.find_all("table")
armor_dsc = tables[2]
#print(armor_dsc)
# retrieves the entire webpage, separating all table elements into a list
# which we subsequently call the one that pertains to the armor
# -----------------------------------------------------------------------
# rows = armor_dsc.find_all("tr")
# for cells in rows:
#     cell_element = cells.find("td")
#     print(cell_element)
row = armor_dsc.find_all("td")
print()
for cell in row:               
    h3_element = cell.find("h3") # change to hr in terminal
    p_element = cell.find_all("p")
    print(h3_element.text) # add .text
    for ds1 in p_element:
        print(ds1.text) # add .text
        #print()
    print()
# note: this one retrieves the entire item description(s) successfully!