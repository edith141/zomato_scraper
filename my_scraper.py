import requests
from bs4 import BeautifulSoup
import pandas
import csv
import re
import json
import sys

headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
# print(page_no)
session = requests.Session()
urls = []
detailsObj = {}
# session.trust_env = False
with open('rlist.txt') as links:
   urls = links.readlines()
#    print(linksList)

for uid,url in enumerate(urls):
    # try:
    T = 5
    while T != 0:
        try:
            response = session.get(f'{url}'.strip()+'/order', headers=headers)
            print(f'{url}'.strip()+'/order')
        # response = requests.get("https://www.zomato.com/bangalore/restaurants?page={}".format(page_no), headers=headers)
            # print(url)
            print(response.status_code)
            content = response.content
            soup = BeautifulSoup(response.text, "lxml")

            food_list = soup.find('section', {'class': 'sc-eqPNPO inpoCu'})
            items = food_list.find_all('div', {'class': 'sc-1s0saks-9 gQuDZH'})
            final_items = []
            for item in items:
                fitem = item.find('h4', {'class': 'sc-1s0saks-11 cDXzZl'})
                fprice = item.find('span', {'class': 'sc-17hyc2s-1 fnhnBd'})
                final_items.append([fitem.text, fprice.text])
                # print([fitem.text, fprice.text])

            detailsObj[url] = final_items
            print(f'SUCCESS! - {uid} - {url}')
        except:
            print(f'ERROR! - {uid} - {url} RETRY-{T}')
            T = T-1
            continue
        break
    # except:
    #     print("Oops!", sys.exc_info()[0], "occurred.")
    #     continue
objJson = json.dumps(detailsObj)
with open(f"bangalore_details.json", "a") as zpage:
    zpage.write(objJson)