from scraper import *
from bs4 import BeautifulSoup

url = "https://www.epicnpc.com/forums/last-cloudia-accounts.1797/"


def main():
    document = collect(url)
    listings = get_listings(document)
    parse_listing(listings[0]['listing_url'])


main()
