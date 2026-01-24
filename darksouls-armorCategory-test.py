import requests
from bs4 import BeautifulSoup

url = "http://darksouls.wikidot.com/armor"
headers = {
    "User-Agent": "DS1 LoreScraper (small, amateur personal project)"
}
page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="page-content")
tables = results.find_all("table")
unlisted = tables[0].find("ul")

links = unlisted.find_all("a")
host_name = "http://darksouls.wikidot.com"

path_ref = [] # fix the unnecessary global line
for link in links:
    path_ref.append(link["href"])
    #print(full_path) # forms complete URL as href is only relative
    

# small test to extract 5 armor descriptions
for i in range(0, 2):
    url2 = host_name + path_ref[i]
    page2 = requests.get(url2, headers=headers)
    soup2 = BeautifulSoup(page2.content, "html.parser")
    results2 = soup2.find(id="page-content")
    page_table = results2.find_all("table")
    # print(page_table)
    armor_dsc = page_table[2]
    
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
    print("-------------------------------------------------------------------------")