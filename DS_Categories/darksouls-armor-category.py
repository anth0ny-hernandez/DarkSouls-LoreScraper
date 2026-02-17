import asyncio
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "http://darksouls.wikidot.com"
HEADERS = {
    "User-Agent": "DS1 LoreScraper (small, amateur personal project)"
}

SEM = asyncio.Semaphore(5)

async def get_page(session, url):
    async with session.get(url) as resp:
        return await resp.text()


async def get_all_descriptions(session, urls):
    descriptions = []
    for url in urls:
        link = url[0]
        descriptions.append(get_single_description(session, link))
    return await asyncio.gather(*descriptions)


async def get_single_description(session, url):
    async with SEM:
        page = await get_page(session, url)
        soup = BeautifulSoup(page, "html.parser")
        div_page = soup.find(id="page-content")
        description_table_cells = div_page.find_all("table")[2].find_all("td")
        armor_set = []
        
        for cell in description_table_cells:
            armor_pce_name = cell.find("h3").get_text()
            pce_descr = cell.find_all("p")
            p_text = ""
            for text in pce_descr:
                p_text += text.get_text()
            armor_set.append([armor_pce_name, p_text])
    # https://www.geeksforgeeks.org/python/python-convert-a-nested-list-into-a-flat-list/
    # to read ^
        return armor_set


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
        urls.append(
            [
                urljoin(BASE_URL, link["href"])
            ]
        ) # note: use url parser
    return urls


async def main():
    async with aiohttp.ClientSession(headers=HEADERS) as session: # maintains single, reusable connection
        armor_urls = await get_all_URLS(session) # retrieves all 58 urls for each respective set
        armor_descriptions = await get_all_descriptions(session, armor_urls) # retrieves individual, unique set descriptions
        for i in range(0, len(armor_urls)):
            armor_urls[i].append(armor_descriptions[i])
            
        for a in armor_urls:
            for element in a:
                if isinstance(element, list):
                    for para in element:
                        # print(para)
                        for sect in para:
                            print(sect)
                else:
                    print(element)
            print("-----------------------------------")
    

asyncio.run(main())