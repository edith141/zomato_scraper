import requests
from bs4 import BeautifulSoup
import pandas
import csv
import re

headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
page_no = 1
list_restaurants =[]

for page in range(0,800):
    try: 
        print(page_no)
        session = requests.Session()
        # session.trust_env = False

        response = session.get(f'https://www.zomato.com/bangalore/restaurants?page={page_no}', headers=headers)
        # response = requests.get("https://www.zomato.com/bangalore/restaurants?page={}".format(page_no), headers=headers)
        print(response.status_code)
        content = response.content
        # print(content)
        soup = BeautifulSoup(content, "lxml")
        search_list = soup.find_all("div", {'id': 'orig-search-list'})
        # print(search_list)
        list_content = search_list[0].find_all("div", {'class': 'content'})
        print('found content on' + str(page_no))
        try:
            for i in range(0,15):
                res_name = list_content[i].find("a", {'data-result-type': 'ResCard_Name'})
                locality = list_content[i].find("b")
                ratings = list_content[i].find("div", {'data-variation': 'mini inverted'})
                if ratings is None:
                    continue
                rest6 = list_content[i].find_all("div", {'class': 'search-page-text clearfix row'})
                rest7 = rest6[0].find_all("span", {'class': 'col-s-11 col-m-12 nowrap pl0'})
                rest8 = rest7[0].find_all("a")
                cuisines = [e.string for e in rest8]
                cost_for_two = rest6[0].find("span", {'class': 'col-s-11 col-m-12 pl0'})
                if cost_for_two is None:
                    continue
                votes = list_content[i].find("span", {'class': re.compile(r'rating-votes-div*')})
                if votes is None:
                    continue
                dataframe ={}
                dataframe["rest_name"] = res_name.string.replace('\n', ' ')
                dataframe["locality"] = locality.string.replace('\n', ' ')
                dataframe["rating"] = ratings.string.replace('\n', ' ')
                dataframe["cuisines"] = cuisines
                dataframe["cost_for_two"] = cost_for_two.string[1:]
                dataframe["votes"] = votes.string.split()[0]
                list_restaurants.append(dataframe)
            page_no+=1
        except:
            page_no+=1
            continue
    except:
        page_no+=1
        continue    
df = pandas.DataFrame(list_restaurants)
df.to_csv("zomato_restaurants.csv")