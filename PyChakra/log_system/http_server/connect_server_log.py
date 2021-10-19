'''

    ABOUT THIS FILE :

    This is used to provide log data
    to http_server.py when a client
    is connecting to the server .

'''

# Provide time for the log data.

import datetime 

class connect_server_log_class:

    # Beginning connection.

    def beginning_connection( host , port ):

        current_time = datetime.datetime.now() 

        host = host

        port = port

        print ("[INFO] [ {y}-{m}-{d} | {h}:{mi}:{s} ] : BEGGINING OF CONNECTION FROM [{host}] . Port [{port}] .".format (

            host = host , 
            port = port ,

            y = current_time.year ,
            m = current_time.month ,
            d = current_time.day ,

            h = current_time.hour ,
            mi = current_time.minute ,
            s = current_time.second
        
            )
    
        )

    # Accept connection.

    def accept_connection( host , port ):

        current_time = datetime.datetime.now() 

        host = host

        port = port

        print ("[INFO] [ {y}-{m}-{d} | {h}:{mi}:{s} ] : Now accepting connection from : [{host}] . Port [{port}]".format (

            host = host , 
            port = port ,

            y = current_time.year ,
            m = current_time.month ,
            d = current_time.day ,

            h = current_time.hour ,
            mi = current_time.minute ,
            s = current_time.second
        
            )
    
        )

    # Send HTTP version and status.

    def send_http_status():

        current_time = datetime.datetime.now() 

        print("[INFO] [ {y}-{m}-{d} | {h}:{mi}:{s} ] : Sending HTTP version and status...".format (
            
            y = current_time.year ,
            m = current_time.month ,
            d = current_time.day ,

            h = current_time.hour ,
            mi = current_time.minute ,
            s = current_time.second

            ) 

        )

    # Send response_header content type.

    def send_type_header():

        current_time = datetime.datetime.now() 

        print("[INFO] [ {y}-{m}-{d} | {h}:{mi}:{s} ] : Sending the content-type of response_header .".format (
            
            y = current_time.year ,
            m = current_time.month ,
            d = current_time.day ,

            h = current_time.hour ,
            mi = current_time.minute ,
            s = current_time.second

            ) 

        )

    # Send response_body .

    def send_response_body():

        current_time = datetime.datetime.now() 

        print("[INFO] [ {y}-{m}-{d} | {h}:{mi}:{s} ] : Sending the response_body .".format (
            
            y = current_time.year ,
            m = current_time.month ,
            d = current_time.day ,

            h = current_time.hour ,
            mi = current_time.minute ,
            s = current_time.second

            ) 

        )



    