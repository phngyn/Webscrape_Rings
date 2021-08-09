import os
import json
import re
import time

from pandas import DataFrame

from urllib3 import response, PoolManager
from bs4 import BeautifulSoup as bs

json_file = "C:\\dev\\Projects\\webscrape_idnid\\data_output.json"

# with open(json_file) as file:
#     data = json.load(file)
#     print(data)
#     for link in data["link"]:
#         print(link)


