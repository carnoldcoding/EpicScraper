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
                'listing_title': row.find("a", {"class": ""}).text.encode("utf-8"),
                'author': row.find("a", {"class": "username"}).text,
                'user_likes': row.tr.text.split("\n")[2],
                'user_ratio': row.find("td", {"class": "sc_itraderbox_td3"}).text,
                'listing_type': row.find("a", {"class": "labelLink"}).text,
                'listing_url': "https://www.epicnpc.com" +
                               row.find("a", {"class": ""}).attrs['data-preview-url'].split("/preview")[0],
                'img_urls': []
            }
            listings.append(listing)
            # print(listing)
            # print("------------------------------------")
    return listings


def only_urls(listings):
    urls = []
    for listing in listings:
        urls.append(listing["listing_url"])
    return urls


def listing_details(listing):
    url = listing['listing_url']
    doc = collect(url)

    wrapper = doc.find("div", {"class": "bbWrapper"})  # Get the wrapper that holds all information

    for image in wrapper.find_all("div", {"class": "bbImageWrapper"}):  # Remove all images from the potential output
        image.decompose()

    for script in wrapper.find_all("script"):  # Remove all scripts from the potential output
        script.decompose()

    # Maybe do the same for img links with the 'a' tag later

    lines = wrapper.get_text()  # Turn information left into text that can be easily displayed

    listing["listing_details"] = ""
    for line in lines.splitlines():
        listing["listing_details"] += line + "\n"
    listing["listing_details"] = listing["listing_details"].encode("ascii", "ignore")


def listing_media(listing):
    doc = collect(listing["listing_url"])
    wrapper = doc.find("div", {"class": "bbWrapper"})  # Get the wrapper that holds all information

    images = wrapper.find_all("img")
    for image in images:
        if "https" in str(image.get('src')) and str(image.get('src')) not in listing["img_urls"] and 'unicode' not in \
                str(image.get('src')):
            listing["img_urls"].append(image.get('src'))

    #  Get attachment images
    try:
        attachments = doc.find("section", {"class": "message-attachments"}).find_all("a")

        for attachment in attachments:
            if attachment.get('href') is not None:
                listing["img_urls"].append(attachment.get('href'))
    except:
        print("No Attachments")

    # Get imgur carousel images
    try:
        imgur_album = doc.find("blockquote", {"class": "imgur-embed-pub"}).find("a").attrs["href"]
        print(imgur_album)

    except:
        print("No Imgur Album")


def display_information(listings):
    for listing in listings:
        print("--" + listing["listing_title"] + "--")
        print("User: " + listing["author"])
        print("Likes: " + listing["user_likes"])
        print("Ratio: " + listing["user_ratio"])
        print(listing["listing_url"])
        print("\n----------------\n")


# These are URLS not Listing Dictionaries
def compare(old_urls, scraped_urls):
    new_urls = []
    for url in scraped_urls:
        if url not in old_urls:
            new_urls.append(url)
    return new_urls

