#!/usr/bin/env python3

'''

    ABOUT THIS FILE :

    app.py wants to transfer status, response_headers,
    response_body to the http_server.py to be processed
    via a function called start_response.

    I decided to " transport " all the parameters to a class,
    then after that I decided to transfer all the class 
    variables to the http_server.py.

'''

from http_server import init_http_server

from log_system.start_server import start_response_log

log = start_response_log.start_response_log_class

# Response class.

class start_response_class:

    host             = None
    port             = None
    status           = None
    response_headers = None 
    response_body    = None
    encoding         = None

'''

    Set host and port to host and port parameters from exec_app.py .
    The reason why Im not combining trans_host_port() and start_response()
    is because at app.py , everyone writes start_response but the parameters
    are only status, headers, and body. You get it.

'''

def pass_host_port_encoding ( host , port , encoding):

    start_response_class.host     = host
    start_response_class.port     = port
    start_response_class.encoding = encoding
    
# Passing status, respons_headers, and response_body to init_http_server() .

def start_response ( status , response_headers  ,response_body ):

    log.exec_start_response()

    '''

         Set all the class variables from parameters 
         variables that was sended from app.py .

    '''

    start_response_class.status           = status
    start_response_class.response_headers = response_headers
    start_response_class.response_body    = response_body

    host                                  = start_response_class.host
    port                                  = start_response_class.port
    encoding                              = start_response_class.encoding

    # Log data for executing init_http_server() .

    log.exec_init_http_server()

    # Execute init_http_server() .

    init_http_server (

        host , 
        port , 
        encoding ,
        start_response_class.status ,
        start_response_class.response_headers , 
        start_response_class.response_body 


    )


    

    

