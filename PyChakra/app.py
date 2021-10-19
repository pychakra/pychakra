#!/usr/bin/env python3

'''

    ABOUT THIS FILE :

    This is the app.py , PyChakra is designed to be modular,
    configurable, and easy - to - use. Developers can easily
    switch app.py with any shit they want and the web still 
    works!

'''

### Application.

from prepare_server import run_server

def application (environ, start_response):

    response_body = [

        # FOR DEMO PURPOSE ONLY ! You can delete 
        # this part if you want. ( Inside """ ) .

        """

            <!DOCTYPE html>

            <html lang="us">

               <head>

                  <title>Demo | PyChakra</title>

               </head>

               <body>

                  <style>

                     /*Style.*/

                     .title {

                         color : black;
                         font-family : Arial, Helvetica, sans-serif;
                         font-size : 50px;
                         font-weight : bold;

                     };

                     .paragraph {

                         color : black;
                         font-family : Arial, Helvetica, sans-serif;

                     };

                     .button {

                         background-color: #0d3b4f;
                         color : white;
                         border : 2px solid black;
                         border-radius : 2px;
                         font-family : Arial, Helvetica, sans-serif;

                     };

                  </style>

                  <!--Title-->

                  <hl1 class = "title">Welcome ! This is a demo.</hl1>

                  <p class="paragraph">

                       PyChakra is an open source Python-based 
                       WSGI HTTP server. The goal of the project
                       is to make a configurable, easy-to-use,
                       lightweight, and simple WSGI HTTP server.

                       Click <a href="https://pychakra.github.io">here</a> 
                       to visit our website.
                  
                  <p>

                  <!--Demo-->

                  <p id="demo"></p>

                  <!--Button-->

                  <button onclick="run()" class="button">Click me!</button>

                  <script>

                     // Console.log

                     console.log("Hello, world!");

                     // Data source for innerHTML.

                     change = () => {

                         var change = "Hello, world!";

                         return change;

                     };

                     // Run to change the innerHTML of "demo" .

                     function run() {

                         document.getElementById("demo").innerHTML = change(); 

                     };             

                  </script>

               </body>

            </html>

        """
    ]

    response_body = '\n'.join(response_body)

    status = '200 OK'

    response_headers = [ ('Content-type', 'text/html') ]

    start_response ( status, response_headers , response_body )

run_server ('0.0.0.0' , 8000 , app = application , encoding = 'utf-8' )



