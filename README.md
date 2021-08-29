# Webscrape IDoNowIDont
IDoNowIDont is a 2nd-hand marketplace for rings, watches, and jewelry. It's like Craigslist or Facebook Marketplace for used jewelry, but the filtering UI is limited.
To get around the design, we use `requests` and `BeautifulSoup4` to parse the marketplace for all listings.

Each listing has a varied number of attributes (e.g. some rings have side stones and have fields for the side stones), so we save the data in dictionary format and export to `json` format.

We can then use `pandas` to output a user-friendly spreadspeed and filter for our desired traits.

## How to use

To start, clone the repo and setup a virtual environment:

```bash
git clone https://github.com/phngyn/idnid
cd idnid

# Optional: setup virtual environment
pip install virtualenv
virtualenv .env
source .env/bin/activate # .\env\Scripts\activate for Windows
```

Next install the dependencies and run `main.py`: 

```bash
# Install requests, beautifulsoup4, and pandas
pip install -r requirements.txt
python main.py
```

`main.py` does the following:
  - Find all marketplaces in [https://www.idonowidont.com/](https://www.idonowidont.com/)
  - For each marketplace, find all listings
  - For each listing, check if the link exists in our data file
  - If the listing doesn't exist in our data file, record the url, price, and all attributes into `output.json`

From here, you can use `pd_reader.py` to create a user-friendly spreadsheet and filter for your desired jewelry traits.

[](images/filtered_data.png)
