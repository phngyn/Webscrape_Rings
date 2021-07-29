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

base_url = "https://www.idonowidont.com/marketplace/engagement-rings"
master_list = dir_path + "\master_list.txt"
data_list = dir_path + "\data_list.txt"

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
    values = target_url + "," + price + "," + carat + "," + clarity + "," + shape + "," + color

    textfile = open(data_list, "a")
    textfile.write(values + "\n")
    textfile.close()


print("test")
print("test")
print("test")
print("test")
