def write_html(listings):
    num = 10

    html = '''
    <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Your Update %d </title>
                <h1 style="text-align: center; color: blue;"> Working well </h1>
            </head>
    ''' % num
    for listing in listings:
        html += '''
        <div style="text-align: center;">
            <h3> Title: %s </h3>
            <p> Author: %s </p>
            <p> User Likes: %s </p>
            <p> User Ratio: %s </p>
            <p> Listing Status: %s </p>
            <a href=%s>Link</a>
        </div>
        ''' % (listing["listing_title"].decode('ascii', 'ignore'), listing["author"], listing["user_likes"],
               listing["user_ratio"], listing["listing_type"],
               listing["listing_url"])

    html += "</html>"
    file = open("update.html", "w")
    file.write(html)
    file.close()
