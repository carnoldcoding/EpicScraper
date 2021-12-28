from scraper import *


def write_html(listings):
    listing_id = -1

    html = '''
    <!DOCTYPE html>
        <html lang="en">
            <head>
              <meta charset="UTF-8">
              <meta name="viewport" content="width=device-width, initial-scale=1.0">
              <title>CarnoldPyBot</title>
              <style>
              * {
              padding: 0;
              margin: 0;
              box-sizing: border-box;
            }
            
            p {
                margin: .5rem;
            }
            
            body {
              background: black;
              font-family: sans-serif;
            }
            
            .container {
              width: 90%;
              margin: 50px auto;
            }
            .heading {
              text-align: center;
              font-size: 30px;
              margin-bottom: 50px;
            }
            
            .row {
              display: flex;
              flex-direction: row;
              justify-content: space-around;
              flex-flow: wrap;
            }
            
            .card {
              width: 20%;
              background: #fff;
              border: 1px solid #ccc;
              margin-bottom: 50px;
              transition: 0.3s;
            }
            
            .card-header {
              text-align: center;
              padding: 50px 10px;
              background: #161d20;
              color: white;
            }
            
            .card-body {
              padding: 30px 20px;
              text-align: center;
              font-size: 18px;
              background-color: #a4a29e
            }
            
            .card-body .img{
              background-color: #a4a29e
              min-width: 17rem;
              max-width: 17rem;
              
              min-height: 30rem;
              max-height: 30rem;
              
              width: 100%;
              height: auto;
              
            }
            
            .card-body .btn {
              display: block;
              color: #fff;
              text-align: center;
              background: linear-gradient(to right, #36498f, #2d7c9d);
              margin-top: 30px;
              text-decoration: none;
              padding: 10px 5px;
            }
            
            .card-body .btn:hover {
              transform: scale(1.05);
              transition: .3s;
              box-shadow: 0 0 40px -10px rgba(0, 0, 0, 0.25);
            }
            
            @media screen and (max-width: 1000px) {
              .card {
                width: 40%;
              }
            }
            
            @media screen and (max-width: 620px) {
              .container {
                width: 100%;
              }
            
              .heading {
                padding: 20px;
                font-size: 20px;
              }
            
              .card {
                width: 80%;
              }
            }
            </style>
            </head>
    '''

    html += '''
                    <script>
                        function nextImage(element, imgArray, index)
                            {
                                console.log(index.index)
                                index.index += 1;
                                document.getElementById(element).src=imgArray[index.index].src;
                                if (index.index == imgArray.length-1){
                                    index.index = 0;
                                }
                            }  
                        </script>
                        <body>
                    '''

    for listing in listings:
        listing_id += 1
        html += '''
              <div class="container">
                <div class="row">
                  <div class="card">
                    <div class="card-header">
                      <h1>%s</h1>
                    </div>
                    <div class="card-body">
                      <p> <b><u>User Info</u></b></p>
                      <p>%s</p>
                      <p> %s Upvotes, %s Positive</p>
                      <p> %s </p>
                      <p> <b><u>Account Details</u></b></p>
                      <p>%s</p>
                    
        
        ''' % (listing["listing_title"].decode('ascii', 'ignore'), listing["author"], listing["user_likes"],
               listing["user_ratio"], listing["listing_type"], listing["listing_details"].decode()[:200] + "...")
        if len(listing["img_urls"]) == 0:
            listing["img_urls"].append("https://tacm.com/wp-content/uploads/2018/01/no-image-available.jpeg")

        for x in range(len(listing["img_urls"])):
            if x == 0:
                html += '''
                <script>
                var img_array_%s = new Array();
                 
                const index_%s = {
                  index: 0  
                };
                
                </script>
                
                <img class = 'img' src = '%s' id = 'img_id_%s' />
                <a class="btn" onclick="nextImage('img_id_%s', img_array_%s, index_%s)">Next Image</a>
                <a href="%s" class="btn" target="_blank" >Go to Listing</a>
                </div>
                </div>
                </div>
                </div>
                
                <script>
                ''' % (listing_id, listing_id, listing["img_urls"][x], listing_id, listing_id, listing_id, listing_id,
                       listing["listing_url"])
            html += '''
            img_array_%s[%s] = new Image();
            img_array_%s[%s].src = '%s'
            ''' % (listing_id, x, listing_id, x, listing["img_urls"][x])

            if x == len(listing["img_urls"]) - 1:
                html += '''</script>'''

    html += " </body> </html>"
    file = open("update.html", "w")
    file.write(html)
    file.close()
