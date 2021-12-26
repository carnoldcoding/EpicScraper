from scraper import *
from fileIO import *
from messenger import *
import os

url = "https://www.epicnpc.com/forums/last-cloudia-accounts.1797/"
file_url = "./output.csv"


def main():
    document = collect(url)
    listings = get_listings(document)
    new_urls = compare(read_urls(file_url),
                       only_urls(listings))  # Compare what's in the file to what was pulled from the web

    send_message("hello")

    # write_urls(listings)


main()
