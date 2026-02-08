import asyncio
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class DarkSouls:

    SEM = asyncio.Semaphore(5)
    headers = {
        "User-Agent": "DS1 LoreScraper (small, amateur personal project)"
    }
    host_url = "http://darksouls.wikidot.com/"
    
    def __init__(self, url):
        self.url = url
    
    async def get_page(self, session, url):
        async with session.get(url) as resp:
            return await resp.text()


    async def get_single_description(self, session, url):
        return
    async def get_all_descriptions(self, session, url):
        return
    async def get_all_urls(self, session):
        page = await self.get_page(session, self.url)
        soup = BeautifulSoup(page, "html.parser")
        return


    async def main():
        async with aiohttp.ClientSession(headers=DarkSouls.headers) as session:
            consumables_url = await DarkSouls.get_all_urls(session)
            consumables_description = await DarkSouls.get_all_descriptions(session, consumables_url)
            print(consumables_description)

    asyncio.run(main())