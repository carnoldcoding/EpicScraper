import bs4.element
from bs4 import BeautifulSoup
import requests


# Send HTTP Request and store the response
# Parse the response with html5lib and beautifulSoup
def collect(url):
    r = requests.get(url)
    # print(r.content)

    doc = BeautifulSoup(r.content, 'html5lib')
    # print(doc.prettify())

    return doc


# Srape/parse information
def scrape(doc):
    posts = doc.find('div', attrs={'class': 'structItemContainer-group js-threadList'}).children
    listings = []
    for row in posts:
        if type(row) is not bs4.element.NavigableString:
            listing = {
                'a': row.a['href']
            }
            print(listing['a'])
