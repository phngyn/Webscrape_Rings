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
1. Pulls all ring attributes

## Done
- The script will pull listings from all categories and all attributes.
- Break up script up into parts instead one run 

## Future plans
- The script needs to detect when a post is removed from the website and remove it from the list
- Detect duplicate entries or update existing entries
- Add error handling for:
    - Invalid links