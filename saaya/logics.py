import requests, json
import aiohttp, asyncio
from bs4 import BeautifulSoup

async def getExternalResults(query):
    GOOGLE_API_BASE_URL = f"https://www.google.com/complete/search?q={query}&client=chrome"
    BING_API_BASE_URL = f"https://www.bing.com/AS/Suggestions?qry={query}&cvid=dontblockmebing"
    DUCKDUCKGO_API_BASE_URL = f"https://duckduckgo.com/ac/?q={query}"

    headers = {
        "Accept":"application/json"
    }
    async with aiohttp.ClientSession() as session:
        urls = [GOOGLE_API_BASE_URL, BING_API_BASE_URL, DUCKDUCKGO_API_BASE_URL]
        results = []
        try:
            responses = await asyncio.gather(*[session.get(url) for url in urls])
            for each_response in responses:
                if each_response.status == 200:
                    google_results = await responses[0].text()
                    bing_results = await responses[1].text()
                    ddg_results = await responses[2].text()

                    soup = BeautifulSoup(bing_results, "html.parser")
                    sa_sg_elements = soup.find_all(class_='sa_sg')

                    final_google_res = json.loads(google_results)[1]
                    final_bing_res = [element.get('query') for element in sa_sg_elements]
                    final_ddg_res = json.loads(ddg_results)
                    final_results = [final_google_res, final_bing_res, [i["phrase"] for i in final_ddg_res]]
                else:
                    final_results.append("Something fishy is going on here, try later!")
        except:
            final_results = None
        return final_results

