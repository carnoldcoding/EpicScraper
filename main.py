from scraper import *
from fileIO import *
from write_html import *
from messenger import *
import os

url = "https://www.epicnpc.com/forums/last-cloudia-accounts.1797/"
file_url = "./output.csv"
results = 10


def main():
    document = collect(url)
    listings = get_listings(document)

    for listing in listings[:results]:
        listing_details(listing)
        listing_media(listing)

    write_urls(listings[:results])
    write_html(listings[:results])
    send_message("Thanks for using CarnoldPyBot v1.00")




main()
