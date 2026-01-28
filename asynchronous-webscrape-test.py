import asyncio
import aiohttp
import time
from random import randint
from bs4 import BeautifulSoup

BASE_URL = "http://darksouls.wikidot.com"
HEADERS = {
    "User-Agent": "DS1 LoreScraper (small, amateur personal project)"
}

async def get_page(session, url):
    async with session.get(url) as resp:
        return await resp.text()


async def get_all_descriptions(session, urls):
    descriptions = []
    for url in urls:
        time.sleep(randint(1, 3))
        page = await get_single_description(session, url)
        descriptions.append(page)
    results = await asyncio.gather(*descriptions)
    return results


async def get_single_description(session, url):
    page = await get_page(session, url)
    soup = BeautifulSoup(page, "html.parser")
    results = soup.find(id="page-content")
    page_table = results.find_all("table")
    armor_dsc = page_table[2]    
    row = armor_dsc.find_all("td")
    print()
    
    for cell in row:               
        h3_element = cell.find("h3")
        p_element = cell.find_all("p")
        print(h3_element.text)
        for ds1 in p_element:
            print(ds1.text)
        print()
    print("-------------------------------------------------------------------------")


async def get_all_URLS(session):
    urls = []
    page = await get_page(session, "http://darksouls.wikidot.com/armor")
    soup = BeautifulSoup(page, "html.parser")
    
    # naviagtes HMTL DOM to find links pertaining to an armor set
    results = soup.find(id="page-content")
    tables = results.find_all("table")
    armor_list = tables[0].find("ul")
    links = armor_list.find_all("a")
    for link in links:
        urls.append(BASE_URL + link["href"]) # note: use url parser
    return urls


async def main():
    async with aiohttp.ClientSession(headers=HEADERS) as session: # maintains single, reusable connection
        armor_urls = await get_all_URLS(session) # retrieves all 58 urls for each respective set
        armor_descriptions = await get_all_descriptions(session, armor_urls) # retrieves individual, unique set descriptions
        print(armor_descriptions)
    

asyncio.run(main())