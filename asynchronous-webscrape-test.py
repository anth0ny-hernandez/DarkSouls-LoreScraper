import asyncio
import aiohttp as aiohttp
import requests
from bs4 import BeautifulSoup

BASE_URL = "http://darksouls.wikidot.com"

# ******** asynchronous scrape START ********

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.text()


async def crawl():
    page = []
    webpage = await fetch("http://darksouls.wikidot.com/armor")
    soup = BeautifulSoup(webpage, "html.parser")
    
    # retrieves the bulleted armor sets
    results = soup.find(id="page-content")
    tables = results.find_all("table")
    armor_list = tables[0].find("ul")
    links = armor_list.find_all("a")
    for link in links:
        page.append(BASE_URL + link["href"])
    
    return page


# *** call scrape(links) ***
# asynchronous function to process all 58 armors more quickly
async def scrape(armorAsycnArray):
    # small test to extract 2 armor descriptions
    # give more unique variable names
    armorAsycnArray = armorAsycnArray[0:10]
    url2 = await fetch(armorAsycnArray)
    soup2 = BeautifulSoup(url2, "html.parser")
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


async def main():
    links = await crawl()
    
    tasks = []
    for link in links:
        tasks.append(scrape(link))
    armors = await asyncio.gather(*tasks)
    
    
asyncio.run(main())
# ******** asynchronous scrape END ********