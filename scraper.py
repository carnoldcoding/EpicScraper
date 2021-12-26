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


# Scrape/parse information
def get_listings(doc):
    posts = doc.find('div', attrs={'class': 'structItemContainer-group js-threadList'}).children
    listings = []
    for row in posts:
        if type(row) is not bs4.element.NavigableString:
            listing = {
                'listing_title': row.find("a", {"class": ""}).text,
                'author': row.find("a", {"class": "username"}).text,
                'user_likes': row.tr.text.split("\n")[2],
                'user_ratio': row.find("td", {"class": "sc_itraderbox_td3"}).text,
                'listing_type': row.find("a", {"class": "labelLink"}).text,
                'listing_url': "https://www.epicnpc.com" + row.find("a", {"class": ""}).attrs['data-preview-url'].split("/preview")[0],
            }
            listings.append(listing)
            # print(listing)
            # print("------------------------------------")
    return listings


def parse_listing(url):
    doc = collect(url)
    print(doc.prettify())
