# Webscrape https://www.idonowidont.com/
IDNID is a 2nd hand marketpalce for rings, watches, and jewlery, but it has a limited filtering interface.
To better find rings or jewelry matching our buy criteria, we use BeautifulSoup4 to parse the marketplace for all posts and their attributes. We can then use pandas to output an Excel-friendly format to filter and search.

## How to use
To start, make sure the program dependencies (BeautifulSoup4 and pandas) are installed:

```pip install -r requirements.txt```

Next run main.py. The program does the following:
  - Find all marketplaces in https://www.idonowidont.com/
  - For each marketplace, find all posts
  - For each post, check if the link exists in our data file
  - If the post doesn't exist, record the url, price, and all attributes into data_output.json
  - Use pandas to convert the data into a dataframe
  - Copy the dataframe into clipboard

From here there, you can paste the data into Excel and filter for the desired fields.