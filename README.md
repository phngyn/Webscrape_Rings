# Webscrape IDoNowIDont
Idinid is a 2nd hand marketpalce for rings, watches, and jewlery. It's like Craigslist or Facebook Marketplace for used jewlery, but the filtering UI is limited.
To get around the clunky design, we use `requests` and `BeautifulSoup4` to parse the marketplace for all listing attributes. Each listing has a varied number of attributes (e.g. some rings have side stones and have fields for the side stones), so we save the data in dictionary format and export to `json` format.
We can then use `pandas` to output a user-friendly spreadspeed and filter for our desired traits.

## How to use

To start, clone the repo and setup a virtual environment:

```bash
git clone https://github.com/phngyn/idnid
cd idnid

# Optional: setup virtual environment
pip install virtualenv
virtualenv .env
source .env/bin/activate
```

Next install the dependencies and run `main.py`: 

```bash
# Install requests, beautifulsoup4, and pandas
pip install -r requirements.txt
python main.py
```

`main.py` does the following:
  - Find all marketplaces in [https://www.idonowidont.com/](https://www.idonowidont.com/)
  - For each marketplace, find all posts
  - For each post, check if the link exists in our data file
  - If the post doesn't exist, record the url, price, and all attributes into `output.json`

From here, use `pd_reader.py` to export a user-friendly spreadsheet and filter for the desired jewlery traits.