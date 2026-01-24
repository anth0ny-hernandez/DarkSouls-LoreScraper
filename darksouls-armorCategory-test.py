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

for link in links:
    path_ref = link["href"]
    print(host_name + path_ref) # forms complete URL as href is only relative
    

# small test to extract 5 armor descriptions
