import os
import json
import re
import time

from pandas import DataFrame

from urllib3 import response, PoolManager
from bs4 import BeautifulSoup as bs

def get_market_posts(url, market, last_page):
    url_list = []
    http = PoolManager()

    for i in range(0, last_page + 1):
        if i == 0:
            MY_URL = url + market
        else:
            MY_URL = url + market + "?page=" + str(i)

        response = http.request("GET", url + market)
        soup_html = bs(response.data, "html.parser")
        posts = soup_html.find_all("div", {"class":"ds-1col"})
            
        for post in posts:
            post_url = post.div.a["href"]
            url_list.append(post_url)
            
    return url_list

def get_markets(url):
    markets = []
    http = PoolManager()
    response = http.request("GET", url)
    soup_html = bs(response.data, "html.parser")
    marketplace = soup_html.find_all("div", {"class":"button-cell"})
    
    for market in marketplace:
        markets.append(market.a["href"])
    
    return markets

def get_last_page(url, market):
    http = PoolManager()
    response = http.request("GET", url + market)
    soup_html = bs(response.data, "html.parser")

    try:
        last_page_url = soup_html.find("li", {"class":"pager__item pager__item--last"}).a["href"]
        # not sure why last page is off by -1, so we add 1
        return int(last_page_url[-2:]) + 1
    except:
        return 0

def get_post_details(url):
    post_details = {}
    post_details["link"] = url
    http = PoolManager()

    try:    
        response = http.request("GET", url)
        soup_html = bs(response.data, "html.parser")
        post_details["price"] = soup_html.find("span", {"class":"product-price"}).get_text()
        cols = soup_html.find_all("div", {"class" : re.compile("attributes*")})
        for fields in cols:
            for element in fields.find_all("li",class_=True):
                key = element['class'][0] 
                value = element.get_text(strip=True)
                post_details[key] = value
    except:
        pass

    return post_details

def write_to_file(input, file):
    with open(file, "a") as file:
        file.write(json.dumps(input) + "\n")
        print( "Added:", input)

def main():
    BASE_URL = "https://www.idonowidont.com"
    markets = get_markets(BASE_URL + "/marketplace/")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_ouput = dir_path + "\\data_output.json"
    all_posts = []

    for market in markets:
        last_page = get_last_page(BASE_URL, market)
        all_posts.extend(get_market_posts(BASE_URL, market, last_page))

    for post in all_posts:
        my_url = BASE_URL + post
        with open(data_ouput, "a+") as data:
            if post in data.read():
                # pass
                print( "Exists:", post)
            else:
                post_details = get_post_details(my_url)
                write_to_file(post_details, data_ouput)
    
    data = []
    with open(data_ouput) as rdata:
        for line in rdata:
            data.append(json.loads(line))
    df = DataFrame(data).to_clipboard()

if __name__ == "__main__":
    start_time = time.time()
    # try:
    main()
    # except:
    #     pass
    print("--- %s seconds ---" % (time.time() - start_time))
