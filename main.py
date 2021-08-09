import os
import json
import re
import time

from pandas import DataFrame

from urllib3 import response, PoolManager
from bs4 import BeautifulSoup as bs

def get_market_posts(market_url, last_page):
    url_list = []
    http = PoolManager()

    for i in range(0, last_page):
        if i == 0:
            MY_URL = market_url
        else:
            MY_URL = market_url + "?page=" + str(i)

        response = http.request("GET", MY_URL)
        soup_html = bs(response.data, "html.parser")
        posts = soup_html.find_all("div", {"class":"ds-1col"})
            
        for post in posts:
            post_url = post.div.a["href"]
            url_list.append(post_url)
            
    return url_list

def get_markets(base_url):
    markets = []
    http = PoolManager()
    response = http.request("GET", base_url)
    soup_html = bs(response.data, "html.parser")
    marketplace = soup_html.find_all("div", {"class":"button-cell"})
    
    for market in marketplace:
        markets.append(market.a["href"])
    
    return markets

def get_last_page(market_url):
    http = PoolManager()
    response = http.request("GET", market_url)
    soup_html = bs(response.data, "html.parser")

    try:
        last_page_url = soup_html.find("li", {"class":"pager__item pager__item--last"}).a["href"]
        # not sure why last page is off by -1, so we add 1
        return int(last_page_url.rsplit("page=", 1)[1])
    except:
        return 0

def get_post_details(post_url):
    post_details = {}
    post_details["link"] = post_url
    http = PoolManager()

    try:    
        response = http.request("GET", post_url)
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

def return_json_values(json_file):
    post_detail = []
    data_values = []
    with open(json_file) as file:
        for line in file:
            data_dict = json.loads(line)
            post_detail.append(data_dict)
        data_values = [value for element in post_detail for value in element.values()]
    return data_values

def main():
    BASE_URL = "https://www.idonowidont.com"
    markets = get_markets(BASE_URL + "/marketplace/")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_ouput = dir_path + "\\data_output.json"
    all_posts = []

    for market in markets:
        my_url = BASE_URL + market
        last_page = get_last_page(my_url)
        post_url = get_market_posts(my_url, last_page)
        all_posts.extend(post_url)

    for post in all_posts:
        my_url = BASE_URL + post
        if my_url in return_json_values(data_ouput):
            all_posts.remove(post)
            print(f"{post} removed.")
        else:
            post_details = get_post_details(my_url)
            write_to_file(post_details, data_ouput)
    
    data_set = []
    with open(data_ouput) as file:
        for line in file:
            data_set.append(json.loads(line))
    df = DataFrame(data_set).to_clipboard()

if __name__ == "__main__":
    start_time = time.time()
    main()
    # test_file = "C:\\dev\\Projects\\webscrape_idnid\\data_output.json"
    # test_str = "https://www.idonowidont.com/jewelry/ted-muehling-hand-cut-indian-moonstone-earrings-649556"
    # print(is_in_json(test_str, test_file))
    print("--- %s seconds ---" % (time.time() - start_time))
