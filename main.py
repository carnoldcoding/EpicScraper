from scraper import *
from fileIO import *
from write_html import *
from messenger import *
import os

url = "https://www.epicnpc.com/forums/last-cloudia-accounts.1797/"
file_url = "./output.csv"


def main():
    document = collect(url)
    listings = get_listings(document)
    for listing in listings[:1]:
        listing_details(listing)
        listing_media(listing)

    write_urls(listings[:1])
    write_html(listings[:1])
    # send_message("Thanks for using CarnoldPyBot v1.00")




main()
