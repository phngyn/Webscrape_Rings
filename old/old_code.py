import bs4
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from pprint import pprint

write_file = "C:\\Users\\phngu\\OneDrive\\dev\\Projects\\webscrape\\rings.txt"

href_collect = []
last_page = 47
for i in range(1, last_page + 1):
    my_url = "https://www.idonowidont.com/marketplace/engagement-rings?page=" + str(i)
    # print(my_url)

    #Opens the webpage, reads it into a container, then closes the client
    uClient = urlopen(my_url)
    page_html = uClient.read()
    uClient.close()

    #Uses soup to parse down to href to get weblink
    soup_html = bs(page_html, "html.parser")
    container = soup_html.findAll("div", {"class":"ds-1col"})

    for i in range(len(container)):
        href_collect.append(container[i].div.a["href"])


# for i in href_collect:
#     print("https://www.idonowidont.com" + i)

rings = []

i = 0


textfile = open(write_file, "a")


for url in href_collect:
    
    target_url = "https://www.idonowidont.com" + url
    #Opens the webpage, reads it into a container, then closes the client
    uClient = urlopen(target_url)
    page_html = uClient.read()
    uClient.close()

    soup_html = bs(page_html, "html.parser")

    try:
        #gets price
        container_price = soup_html.find("span", {"class":"product-price"})
        price = container_price.get_text()
    except:
        pass

    try:
        #gets carat
        container_carat = soup_html.find("li", {"class":"field_carat_weight"})
        carat = container_carat.div.div.get_text()
    except:
        pass
    
    try:
        #gets clarity
        container_clarity = soup_html.find("li", {"class":"field_clarity"})
        clarity = container_clarity.div.div.get_text()
    except:
        pass

    try:
        #gets shape
        container_shape = soup_html.find("li", {"class":"field_shape"})
        shape = container_shape.div.div.get_text()
    except:
        pass

    try:
        #gets color
        container_color = soup_html.find("li", {"class":"field_color"})
        color = container_color.div.div.get_text()
    except:
        pass

    # values = []
    # values = [target_url, price, carat, clarity, shape, color]
    values = target_url + "," + price + "," + carat + "," + clarity + "," + shape + "," + color


    textfile = open(write_file, "a")
    textfile.write(values + "\n")
    textfile.close()

    

    # rings.append(values)

# print(rings)

#Build logic to check if new ring is already in master list
#If new ring is in master list, ignore ring
#if new ring is not in master list, mine data and append to masterlist

import os
import bs4
import urllib

from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup as bs
from pprint import pprint


container_posting_url = []
#gets directory of current working file
dir_path = os.path.dirname(os.path.realpath(__file__))

base_url = "https://www.idonowidont.com/marketplace/men's-watches"
master_list = dir_path + "\master_list_watches.txt"
data_list = dir_path + "\data_list_watches.txt"

print(master_list, data_list)

#Find the last page to loop through
uClient = urlopen(base_url)
page_html = uClient.read()
uClient.close()
soup_html = bs(page_html, "html.parser")
last_page_url = soup_html.find("li", {"class":"pager__item pager__item--last"}).a["href"] 

# not sure why last page is off by -1, so we add 1
last_page = int(last_page_url[-2:]) + 1


# Loop through list of pages to gather all posting url
# and add url to our master_list if it's not in the file
for i in range(0, last_page + 1):
    if i == 0:
        my_url = base_url
    else:
        my_url = base_url + "?page=" + str(i)
    
    print(my_url)

    #Opens the webpage, reads it into a container, then closes the client
    uClient = urlopen(my_url)
    page_html = uClient.read()
    uClient.close()

    #Uses soup to parse down to href to get weblink
    soup_html = bs(page_html, "html.parser")
    container_posting = soup_html.findAll("div", {"class":"ds-1col"})

    for posts in container_posting:
        post_url = posts.div.a["href"]
        with open(master_list, "r+") as file:
            if post_url in file.read():
                pass
            else:
                file.write(post_url + "\n")


# Read master_list and check if link is valid
# if valid, continue with data mine
# if invalid, remove from master_list

with open(master_list) as f:
    master_list_urls = [line.rstrip() for line in f]
    print(master_list_urls)

with open(data_list) as g:
    data_list_urls = [line.rstrip() for line in g]
    print(data_list_urls)

for url in master_list_urls:
    target_url = "https://www.idonowidont.com" + url
    print(target_url)

    with urlopen(target_url) as client:
        if client.status != 200 and target_url not in data_list_urls:
            pass
        else:
            page_html = client.read()

    soup_html = bs(page_html, "html.parser")

    try:
        #gets price
        container_price = soup_html.find("span", {"class":"product-price"})
        price = container_price.get_text()
    except:
        pass

    try:
        #gets carat
        container_carat = soup_html.find("li", {"class":"field_carat_weight"})
        carat = container_carat.div.div.get_text()
    except:
        pass
    
    try:
        #gets clarity
        container_clarity = soup_html.find("li", {"class":"field_clarity"})
        clarity = container_clarity.div.div.get_text()
    except:
        pass

    try:
        #gets shape
        container_shape = soup_html.find("li", {"class":"field_shape"})
        shape = container_shape.div.div.get_text()
    except:
        pass

    try:
        #gets color
        container_color = soup_html.find("li", {"class":"field_color"})
        color = container_color.div.div.get_text()
    except:
        pass

    # values = []
    # values = [target_url, price, carat, clarity, shape, color]
    values = target_url + "|" + price + "|" + carat + "|" + clarity + "|" + shape + "|" + color

    textfile = open(data_list, "a")
    textfile.write(values + "\n")
    textfile.close()


import os

dir_path = os.path.dirname(os.path.realpath(__file__))

ring_src = dir_path + "\\ring_src.txt"
ring_data = dir_path + "\\ring_data.txt"

with open(ring_src) as f:
    ring_src_lines = [line.rstrip() for line in f]

with open(ring_data) as g:
    ring_data_lines = [line.rstrip() for line in g]

# print(ring_data_lines)

for line in ring_src_lines:
    with open(ring_data) as data:
        if line in data.read():
            print("True")