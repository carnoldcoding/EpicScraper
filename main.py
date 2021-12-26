from scraper import *
from bs4 import BeautifulSoup

url = "https://www.epicnpc.com/forums/last-cloudia-accounts.1797/"


def main():
    document = collect(url)
    scrape(document)


main()
