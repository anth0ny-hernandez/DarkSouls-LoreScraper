import asyncio
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urljoin

host_url = "http://darksouls.wikidot.com/rings"
domain_name = "http://darksouls.wikidot.com"
headers = {
    "User-Agent": "DS1 LoreScraper (small, amateur personal project)"
}

async def get_page(session, url):
    async with session.get(url) as resp:
        return await resp.text()
    

async def get_single_description(session, url):
    page = await get_page(session, url)
    soup = BeautifulSoup(page, "html.parser")
    results = soup.find(id="page-content")
    ring_descr = results.find_all("p")
    # due to the 'p' element separating the complete
    # descriptions, we must iterate through the elements
    # print(ring_descr[0])
    # print(ring_descr[1])
    ring_descr_set = ring_descr[0].text + "\n" + ring_descr[1].text
    return ring_descr_set


async def get_all_descriptions(session, urls):
    descriptions = []
    for ring_data in urls:
        link = ring_data[0]
        # print(link)
        page = await get_single_description(session, link)
        descriptions.append(page)
    results = await asyncio.gather(*descriptions)
    return results


async def get_all_URLS(session):
    page = await get_page(session, host_url)
    soup = BeautifulSoup(page, "html.parser")
    ring_table = soup.find(class_="wiki-content-table")
    rows = ring_table.find_all("tr")
    rows = rows[1:] # slices out row of table headers
    
    ring_data = [] # will be a 2D array to hold 4 attributes
    for link in rows:
        ring = link.find_all("td")
        ring_data.append(
            [
                urljoin(domain_name, link.find("a")["href"]),
                ring[1].text,
                ring[2].text,
                ring[3].text
            ]
        )
    
    return ring_data


async def main():
    async with aiohttp.ClientSession(headers=headers) as session:
        # functions are ordered the same way they're executed here,
        # to better follow, understand, & to stay organizated
        # e.g., here: top-->bottom; actual functions: bottom-->top
        ring_urls = await get_all_URLS(session)
        ring_description = await get_all_descriptions(session, ring_urls)
        print(ring_description)


asyncio.run(main())
