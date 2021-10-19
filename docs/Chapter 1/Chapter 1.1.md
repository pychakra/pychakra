# Chapter 1.1 - Getting Started

Go to the folder PyChakra, edit the file caleed "app.py" 
( Without the quotation marks of course ) .

If you have a sufficient knowledge about networking,
internet, and web... you will recognize all the scripts.

response_body contains the content of the web.

content-type of response_headers contains well, 
content-type of the web content. Which I set to HTML.

status itself is the status of the server.

This import command will import the function that
starts the server ( Without the quotation marks ) :

"from prepare_server import run_server"

After that, make sure when running run_server, it has
4 parameters ( Without the quotation marks ) :

"run_server ('0.0.0.0' , 8000 , app = application , encoding = 'utf-8' )"

- Server host.
- Server port.
- Function that is used to provide the data.
- Encoding methods, in my case, I used utf-8 .

Unlike Gunicorn, start_response is different.

"start_response ( status, response_headers , response_body )"

3 Parameters:

- Server status    : Which describes the status of the server ( '200 OK' )
- response_headers : Which describes the server content-type.
- response_body    : Which describes the server web content.

No return statement at all.

For the source code, Im going to explain it later.
