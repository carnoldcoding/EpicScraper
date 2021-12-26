def write_html(listings):
    num = 10

    html = '''
    <!DOCTYPE html>
        <html lang="en">
            <head>
              <meta charset="UTF-8">
              <meta name="viewport" content="width=device-width, initial-scale=1.0">
              <title>CarnoldPyBot</title>
              <style>* {
              padding: 0;
              margin: 0;
              box-sizing: border-box;
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
            
            .card-body .btn {
              display: block;
              color: #fff;
              text-align: center;
              background: linear-gradient(to right, #36498f, #2d7c9d);
              margin-top: 30px;
              text-decoration: none;
              padding: 10px 5px;
            }
            
            .card:hover {
              transform: scale(1.05);
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
    for listing in listings:
        html += '''
        <body>
              <div class="container">
                <div class="row">
                  <div class="card">
                    <div class="card-header">
                      <h1>%s</h1>
                    </div>
                    <div class="card-body">
                      <p>
                        User: %s <br>
                        Upvotes: %s <br>
                        Ratio: %s <br>
                        Listing: %s
                      </p>
                      <a href="%s" class="btn">Go to Listing</a>
                    </div>
                  </div>
                  </div>
                  </div>
        </body>
        
        ''' % (listing["listing_title"].decode('ascii', 'ignore'), listing["author"], listing["user_likes"],
               listing["user_ratio"], listing["listing_type"],
               listing["listing_url"])

    html += "</html>"
    file = open("update.html", "w")
    file.write(html)
    file.close()
