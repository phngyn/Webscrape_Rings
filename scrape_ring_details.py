import os
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

BASE_URL = "https://www.idonowidont.com/marketplace/engagement-rings"

dir_path = os.path.dirname(os.path.realpath(__file__))
ring_src = dir_path + "\\ring_src.txt"
ring_data = dir_path + "\\ring_data.txt"

# Read ring_src and check if link is valid
# if valid, continue with data mine
# if invalid, remove from ring_src
with open(ring_src) as f:
    ring_src_lines = [line.rstrip() for line in f]

for url in ring_src_lines:
    target_url = "https://www.idonowidont.com" + url

    with open(ring_data) as data:
        if target_url in data.read():
            print( "Exists:", target_url)
        else:
            try:
                ring_fields = {}
                ring_fields["link"] = target_url
                with urlopen(target_url) as client:
                    page_html = client.read()
                    soup_html = bs(page_html, "html.parser")
                    ring_fields["price"] = soup_html.find("span", {"class":"product-price"}).get_text()
                    cols = soup_html.find_all("div", {"class":"attributes col-md-4"})
                    for fields in cols:
                        for element in fields.find_all("li",class_=True):
                            # print(element['class'][0])
                            key = element['class'][0] 
                            value = element.get_text(strip=True)
                            ring_fields[key] = value
                    with open(ring_data, "a") as data:
                        data.write(json.dumps(ring_fields) + "\n")
                        print("Added:", ring_fields)
            except:
                pass