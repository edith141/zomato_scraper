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

response = session.get(f'https://www.zomato.com/bangalore/restaurants?page=2', headers=headers)
# response = requests.get("https://www.zomato.com/bangalore/restaurants?page={}".format(page_no), headers=headers)
print(response.status_code)
content = response.content
print(content)