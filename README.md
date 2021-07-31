# Webscrape from https://www.idonowidont.com/

## About website
IDNID is a 2nd hand marketpalce for rings, watches, and jewlery.
The marketplace has the below categories:
  - Engagement rings (most popular)
  - Loose diamonds
  - Men's wedding bands
  - Women's wedding bands
  - Men's watches
  - Women's watches
  - Fine jewelry
  - Vintage Jewelry
  - Wedding dresses
  - Designer dresses

## Current version
The current python script:
1. Loops through the engagement ring pages
1. Records each post url into a text file
1. Loops through each ring and collects:
    1. Price
    1. Carat
    1. Clarity
    1. Shape
    1. Color

## Future plans
- The script will pull listings from all categories and all attributes.
- The script needs to detect when a post is removed from the website and remove it from the list
- Detect duplicate entries or update existing entries
- Break up script up into parts instead one run 
- Add error handling for:
    - Invalid links