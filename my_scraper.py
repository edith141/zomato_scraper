import requests
from bs4 import BeautifulSoup
import pandas
import csv
import re

headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
# print(page_no)
session = requests.Session()
# session.trust_env = False

response = session.get(f'https://www.zomato.com/lucknow/dastarkhwan-1-kaiserbagh/order', headers=headers)
# response = requests.get("https://www.zomato.com/bangalore/restaurants?page={}".format(page_no), headers=headers)
print(response.status_code)
content = response.content
soup = BeautifulSoup(response.text, "lxml")
# with open("zom_page.html", "a") as zpage:
    # zpage.write(str(soup))
    # zpage.close()
food_list = soup.find('section', {'class': 'sc-eqPNPO inpoCu'})
# items = food_list.find_all('h4', {'class': 'sc-1s0saks-11 cDXzZl'})
items = food_list.find_all('div', {'class': 'sc-1s0saks-9 gQuDZH'})
final_items = []
for item in items:
    fitem = item.find('h4', {'class': 'sc-1s0saks-11 cDXzZl'})
    fprice = item.find('span', {'class': 'sc-17hyc2s-1 fnhnBd'})
    final_items.append([fitem, fprice])
    print([fitem.text, fprice.text])

with open("zom_page_flist.html", "w") as zpage:
    zpage.write(str(final_items))
    zpage.close()

