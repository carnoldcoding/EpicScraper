def write_html(listings):
    num = 10

    html = '''
    <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Your Update </title>
                <style>
                body {background-color: black;}
                h1 {
                color: white;
                }
                h3 {
                color: white;
                }
                p{
                color: white;
                border: 1px solid white;
                }
                
                .container{
                display: flex
                }
                .container > * {flex-basis: 100%;}
                
                    
                </style>
                <h1> EpicNPC Update </h1>
            </head>
    '''
    for listing in listings:
        html += '''
        <div class="container">
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
