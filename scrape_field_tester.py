import os
import json
import re
import pprint
from typing import Text

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

MY_URL = "https://www.idonowidont.com/diamonds/blue-nile-custom-engagement-ring-high-quality-single-diamond-730555"

dir_path = os.path.dirname(os.path.realpath(__file__))
tar_file = dir_path + "\\wip\\tester.txt"

ring_fields = {}
ring_fields["link"] = MY_URL
ring_fields["price"] = MY_URL

with urlopen(MY_URL) as client: 
    page_html = client.read()
    soup_html = bs(page_html, "html.parser")
    ring_fields["price"] = soup_html.find("span", {"class":"product-price"}).get_text()
    cols = soup_html.find_all("div", {"class":"attributes col-md-4"})
    for fields in cols:
        for element in fields.find_all("li",class_=True):
            key = element['class'][0] 
            value = element.get_text(strip=True)
            ring_fields[key] = value
    with open(tar_file, "a") as data:
        data.write(json.dumps(ring_fields) + "\n")
        print("Added:", ring_fields)
