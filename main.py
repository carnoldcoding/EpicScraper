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
    new_urls = compare(read_urls(file_url),
                       only_urls(listings))  # Compare what's in the file to what was pulled from the web
    write_html(listings)
    # send_message("Thanks for using CarnoldPyBot v1.00")

    # write_urls(listings)


main()
