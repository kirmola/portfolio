# until asyncio and aiohttp are fixed
from concurrent.futures import ThreadPoolExecutor
import requests, json
# import aiohttp, asyncio
from bs4 import BeautifulSoup

def fetch_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
    return None

def getExternalResults(query):
    GOOGLE_API_BASE_URL = f"https://www.google.com/complete/search?q={query}&client=chrome"
    BING_API_BASE_URL = f"https://www.bing.com/AS/Suggestions?qry={query}&cvid=dontblockmebing"
    DUCKDUCKGO_API_BASE_URL = f"https://duckduckgo.com/ac/?q={query}"

    urls = [GOOGLE_API_BASE_URL, BING_API_BASE_URL, DUCKDUCKGO_API_BASE_URL]
    final_results = []

    with ThreadPoolExecutor(max_workers=30) as executor:
        responses = executor.map(fetch_data, urls)

    for url, response in zip(urls, responses):
        if response:
            if url == GOOGLE_API_BASE_URL:
                google_results = response
            elif url == BING_API_BASE_URL:
                bing_results = response
            elif url == DUCKDUCKGO_API_BASE_URL:
                ddg_results = response

    soup = BeautifulSoup(bing_results, "html.parser")
    sa_sg_elements = soup.find_all(class_='sa_sg')
    final_google_res = json.loads(google_results)[1]
    final_bing_res = [element.get('query') for element in sa_sg_elements]
    final_ddg_res = json.loads(ddg_results)
    final_results = [final_google_res, final_bing_res, [i["phrase"] for i in final_ddg_res]]

    return final_results

    # async with aiohttp.ClientSession() as session:
    #     urls = [GOOGLE_API_BASE_URL, BING_API_BASE_URL, DUCKDUCKGO_API_BASE_URL]
    #     results = []
    #     try:
    #         responses = await asyncio.gather(*[session.get(url) for url in urls])
    #         for each_response in responses:
    #             if each_response.status == 200:
    #                 google_results = await responses[0].text()
    #                 bing_results = await responses[1].text()
    #                 ddg_results = await responses[2].text()

    #                 soup = BeautifulSoup(bing_results, "html.parser")
    #                 sa_sg_elements = soup.find_all(class_='sa_sg')

    #                 final_google_res = json.loads(google_results)[1]
    #                 final_bing_res = [element.get('query') for element in sa_sg_elements]
    #                 final_ddg_res = json.loads(ddg_results)
    #                 final_results = [final_google_res, final_bing_res, [i["phrase"] for i in final_ddg_res]]
    #             else:
    #                 final_results.append("Something fishy is going on here, try later!")
    #     except:
    #         final_results = None
    #     return final_results

