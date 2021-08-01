import os

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

BASE_URL = "https://www.idonowidont.com/marketplace/engagement-rings"

dir_path = os.path.dirname(os.path.realpath(__file__))
ring_src = dir_path + "\\ring_src.txt"
ring_data = dir_path + "\\ring_data.txt"
# print(ring_src, ring_data)

#Find the last page on the website to know our loop range

with urlopen(BASE_URL) as client:
    page_html = client.read()
    soup_html = bs(page_html, "html.parser")
    last_page_url = soup_html.find("li", {"class":"pager__item pager__item--last"}).a["href"]
    # not sure why last page is off by -1, so we add 1
    last_page = int(last_page_url[-2:]) + 1

# Loop through list of pages to gather all ring post url
# and add url to our ring_src if it's not in the file
for i in range(0, last_page + 1):
    if i == 0:
        MY_URL = BASE_URL
    else:
        MY_URL = BASE_URL + "?page=" + str(i)
    print(MY_URL)

    with urlopen(MY_URL) as client:
        page_html = client.read()
        soup_html = bs(page_html, "html.parser")
        container_posting = soup_html.find_all("div", {"class":"ds-1col"})

    for posts in container_posting:
        post_url = posts.div.a["href"]
        with open(ring_src, "r+") as file:
            if post_url in file.read():
                print( "Exists:", post_url)
            else:
                file.write(post_url + "\n")
                print( "Added:", post_url)

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
                with urlopen(target_url) as client:
                    page_html = client.read()
                    soup_html = bs(page_html, "html.parser")

                    try:
                        container_price = soup_html.find("span", {"class":"product-price"})
                        price = container_price.get_text()
                    except:
                        price = "null"

                    try:
                        container_carat = soup_html.find("li", {"class":"field_carat_weight"})
                        carat = container_carat.div.div.get_text()
                    except:
                        carat = "null"

                    try:
                        container_clarity = soup_html.find("li", {"class":"field_clarity"})
                        clarity = container_clarity.div.div.get_text()
                    except:
                        clarity = "null"

                    try:
                        container_shape = soup_html.find("li", {"class":"field_shape"})
                        shape = container_shape.div.div.get_text()
                    except:
                        shape = "null"

                    try:
                        container_color = soup_html.find("li", {"class":"field_color"})
                        color = container_color.div.div.get_text()
                    except:
                        color = "null"

                    try:
                        container_cut = soup_html.find("li", {"class":"field_cut"})
                        cut = container_cut.div.div.get_text()
                    except:
                        cut = "null"

                    values = target_url + "|" + price + "|" + carat + "|" + clarity + "|" + shape + "|" + color + "|" + cut 

                    with open(ring_data, "a") as data:
                        data.write(values + "\n")
                        print("Added:", values)
            except:
                pass

    
