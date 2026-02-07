import requests
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "http://darksouls.wikidot.com/rings"
headers = {
    "User-Agent": "DS1 LoreScraper (small, amateur personal project)"
}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="page-content") # may not even be necessary given table class
ring_table = results.find(class_="wiki-content-table")
rows = ring_table.find_all("tr") # navigates all rows
rows = rows[1:] # slices out row of table headers

host_name = "http://darksouls.wikidot.com"

dragoncrestring = rows[0].find("a")["href"]
# consider making a 2D array for better readability
ring_urls, name, use, availability = [], [], [], []
for ring in rows:
    link = ring.find("a")["href"]
    ring_urls.append(urljoin(host_name, link))
    table_info = ring.find_all("td")
    name.append(table_info[1].text)
    use.append(table_info[2].text)
    availability.append(table_info[3].text)
     
for link in ring_urls:
    print(link)
# for i in range(0, 2):
#     url2 = ring_urls[i]
#     page2 = requests.get(url2, headers=headers)
#     soup2 = BeautifulSoup(page2.content, "html.parser")
#     results2 = soup2.find(id="page-content")
#     # page_table = results2.find_all("table")
#     paragraphs = results2.find_all("p")
#     print(name[i])
#     print(use[i])
#     print(availability[i])
#     # print(paragraphs[0].text + "\n" + paragraphs[1].text)
#     print(paragraphs[0].text)
#     print(paragraphs[1].text)
#     #print(paragraphs[1].text)
#     print()
# # print(len(ring_urls))