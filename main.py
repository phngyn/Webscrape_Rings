"""
Using beautifulsoup4 to parse data from https://www.idonowidont.com/.
"""

import os
import json
import re
import time

from pandas import DataFrame

from urllib3 import PoolManager
from bs4 import BeautifulSoup as bs

def get_market_posts(market_url, last_page):
    """Returns the list of all post urls from a market."""
    url_list = []
    http = PoolManager()

    for i in range(0, last_page):
        if i == 0:
            my_url = market_url
        else:
            my_url = market_url + "?page=" + str(i)

        http_response = http.request("GET", my_url)
        soup_html = bs(http_response.data, "html.parser")
        posts = soup_html.find_all("div", {"class":"ds-1col"})

        for post in posts:
            post_url = post.div.a["href"]
            url_list.append(post_url)

    return url_list

def get_markets(base_url):
    """Returns a list of markets found in the website."""
    markets = []
    http = PoolManager()
    http_response = http.request("GET", base_url)
    soup_html = bs(http_response.data, "html.parser")
    marketplace = soup_html.find_all("div", {"class":"button-cell"})
    for market in marketplace:
        markets.append(market.a["href"])

    return markets

def get_last_page(market_url):
    """Tries to find the last page in the marketplace.
    Used for looping through the range of market pages."""
    http = PoolManager()
    http_response = http.request("GET", market_url)
    soup_html = bs(http_response.data, "html.parser")

    try:
        last_page_url = soup_html.find("li", {"class":"pager__item pager__item--last"}).a["href"]
        # not sure why last page is off by -1, so we add 1
        return int(last_page_url.rsplit("page=", 1)[1])
    except: # pylint: disable=W0702
        return 0

def get_post_details(post_url):
    """Retrieves all post attributes from the the target url."""
    post_details = {}
    post_details["link"] = post_url
    http = PoolManager()

    try:
        http_response = http.request("GET", post_url)
        soup_html = bs(http_response.data, "html.parser")
        post_details["price"] = soup_html.find("span", {"class":"product-price"}).get_text()
        cols = soup_html.find_all("div", {"class" : re.compile("attributes*")})
        for fields in cols:
            for element in fields.find_all("li",class_=True):
                key = element['class'][0]
                value = element.get_text(strip=True)
                post_details[key] = value
    except: # pylint: disable=W0702
        pass

    return post_details

def write_to_file(value_input, data_file):
    """Writes data to target file."""
    with open(data_file, "a") as file:
        file.write(json.dumps(value_input) + "\n")
        print( "Added:", value_input)

def get_links_in(json_file):
    """Returns the list of post urls (key: 'links') in data file."""
    # post_detail = []
    data_values = []
    with open(json_file) as file:
        for line in file:
            data_dict = json.loads(line)
            data_values.append(data_dict["link"])
        # data_values = [value for element in post_detail for value in element.values()]
    return data_values

def main():
    """ main function called to:
    Find all marketplaces in https://www.idonowidont.com/
    For each marketplace, find all posts
    For each post, check if the link exists in our data file
    If the post doesn't exist, record the url, price, and all attributes into data_output.json
    Use pandas to convert the data into a dataframe
    Copy the dataframe into clipboard
    """
    base_url = "https://www.idonowidont.com"
    markets = get_markets(base_url + "/marketplace/")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_ouput = dir_path + "\\data_output.json"
    all_posts = []

    for market in markets:
        my_url = base_url + market
        last_page = get_last_page(my_url)
        post_url = get_market_posts(my_url, last_page)
        all_posts.extend(post_url)

    for post in all_posts:
        my_url = base_url + post
        data_check = get_links_in(data_ouput)
        if my_url in data_check:
            all_posts.remove(post)
            # print(f"{post} removed.")
        else:
            post_details = get_post_details(my_url)
            write_to_file(post_details, data_ouput)

    data_set = []
    with open(data_ouput) as file:
        for line in file:
            data_set.append(json.loads(line))
    DataFrame(data_set).to_clipboard()

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
