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
    
    def __init__(self, url, html_type, html_id):
        self.url = url
        self.html_type = html_type
        self.html_id = html_id


    async def get_page(self, session, url):
        async with session.get(url) as resp:
            return await resp.text()


    async def get_single_description(self, session, link):
        async with self.SEM:
            page = await self.get_page(session, link)
            soup = BeautifulSoup(page, "html.parser")
            h2_results = soup.find(id="page-content").find("h2")
            # due to varying degrees of information, the only constant
            # is that it all lies between two <h2> elements. 
            # ergo, we extract whatever is in between those two.
            p_tags = ""
            for sibling in h2_results.find_next_siblings():
                if sibling.name == "h2":
                    break
                else:
                    # some text doesn't get a new line due to said
                    # new line only being separated by a new <p>
                    # rather than <br> (\n).
                    # see if it can be fixed in the future *
                    p_tags += sibling.get_text()
            return p_tags
    
    
    async def get_all_descriptions(self, session, urls):
        descriptions = []
        for page in urls:
            link = page[0]
            descriptions.append(self.get_single_description(session, link))
        return await asyncio.gather(*descriptions)
    
    
    async def get_all_urls(self, session, id_type, element):
        page = await self.get_page(session, self.url)
        soup = BeautifulSoup(page, "html.parser")
        table_data = []
        #urls = [] # for the inevitable list of urls
        match id_type: # RETURN TO ADD OTHER CASES LATER
            case "class":
                table_html = soup.find_all(class_=element)
                for table in table_html:
                    rows = table.find_all("tr")[1:] 
                    # truncates table headers (*TO WORK ON)
                    # rows = table.find_all("tr")
                    headers = table.find_all("tr")[0].find_all("th")
                    abs_cols = ('Name', 'Use', 'Description', 'Location', 'Location/Trainer', 'Availability')
                    skip_cols_pos = []
                    # for header in rows[0]:
                        # if header == 'Uses' or 'Slots':
                    for i in range(0, len(headers)):
                        if headers[i].text not in abs_cols:
                            skip_cols_pos.append(i)
                    skip_cols = tuple(skip_cols_pos)
                            
                    # END OF *TO WORK ON
                    for row in rows:
                        consume = row.find_all("td")
                        # Due to wiki tables sharing the class 'wiki-content-table',
                        # and the possibility that only one table (per page) may be
                        # of relevance, this skips tables without a hyperlink
                        # by checking the first row's item name
                        if(consume[1].find("a") != None):
                            table_data.append(
                                [
                                    urljoin(self.host_url, row.find("a")["href"]),
                                    consume[0].find("img")["src"],
                                    # unpacks iterated list; noticed that some page's
                                    # table rows have 4 or 5 column values
                                    # *[consume[i].text for i in range(1, len(consume))]
                                    *[consume[i].text for i in range(1, len(consume)) if i not in skip_cols]
                                ]
                            )
                        else:
                            continue
        return table_data


    async def main(self):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            consumables_url = await self.get_all_urls(session, self.html_type, self.html_id)
            consumables_description = await self.get_all_descriptions(session, consumables_url)
            # print(consumables_description)
            # now we match every entry in the url list to their respective item description list
            for i in range(len(consumables_url)):
                consumables_url[i].append(consumables_description[i])
            return consumables_url
            # for i in consumables_url:
            #     # for j in i:
            #     #     print(j)
            #     print(i)

    def run(self):
        return asyncio.run(self.main())