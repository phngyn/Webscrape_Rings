""" import os
import json
import re
import pprint
from typing import Text

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

MY_URL = "https://www.idonowidont.com/jewelry/mikimoto-vintage-strand-pearls-730918"

dir_path = os.path.dirname(os.path.realpath(__file__))
tar_file = dir_path + "\\wip\\tester.txt"

ring_fields = {}
ring_fields["link"] = MY_URL
ring_fields["price"] = MY_URL

with urlopen(MY_URL) as client: 
    page_html = client.read()
    soup_html = bs(page_html, "html.parser")
    ring_fields["price"] = soup_html.find("span", {"class":"product-price"}).get_text()
    cols = soup_html.find_all("div", {"class" : re.compile("attributes*")})
    for fields in cols:
        for element in fields.find_all("li",class_=True):
            key = element['class'][0] 
            value = element.get_text(strip=True)
            ring_fields[key] = value
    with open(tar_file, "a") as data:
        data.write(json.dumps(ring_fields) + "\n")
        print("Added:", ring_fields)
 """
"""
    with urlopen(url) as client:
            page_html = client.read()
            soup_html = bs(page_html, "html.parser")
            marketplace = soup_html.find_all("div", {"class":"button-cell"})
        for market in marketplace:
            markets.append(market.a["href"])
        return markets
"""
import urllib3
import re

from bs4 import BeautifulSoup as bs
from urllib3 import response, PoolManager

""" 
    def get_markets(url):
        http = PoolManager()
        markets = []

        response = http.request("GET", url)
        soup_html = bs(response.data, "html.parser")
        marketplace = soup_html.find_all("div", {"class":"button-cell"})
        
        for market in marketplace:
            markets.append(market.a["href"])
        
        return markets
 """


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

print(get_post_details("https://www.idonowidont.com/jewelry/pearl-ring-692766"))