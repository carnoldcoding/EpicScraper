def write_urls(listings):
    file = open("output.csv", "w")
    for listing in listings:
        file.write(listing["listing_url"] + ",")
    file.close()


def read_urls(file_url):
    file = open(file_url, "r")
    urls = file.readlines()
    try:
        temp = urls[0].split(',')
        urls = temp
    except IndexError:
        print("File is empty, index out of bounds")
    file.close()
    return urls
