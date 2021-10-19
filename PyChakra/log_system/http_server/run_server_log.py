'''

    ABOUT THIS FILE :

    This is used to provide log data
    to http_server .

'''

# Provide time for the log data.

import datetime 

class run_server_log_class:

    # Start server.

    def start_server():

        current_time = datetime.datetime.now() 

        print("[INFO] [ {y}-{m}-{d} | {h}:{mi}:{s} ] : Starting the server...".format (
            
            y = current_time.year ,
            m = current_time.month ,
            d = current_time.day ,

            h = current_time.hour ,
            mi = current_time.minute ,
            s = current_time.second

            ) 

        )

    # Getting all the info.

    def getting_server_info():

        current_time = datetime.datetime.now() 

        print("[INFO] [ {y}-{m}-{d} | {h}:{mi}:{s} ] : Getting all the information of the server...".format (
            
            y = current_time.year ,
            m = current_time.month ,
            d = current_time.day ,

            h = current_time.hour ,
            mi = current_time.minute ,
            s = current_time.second

            ) 

        )

    # Create socket.

    def create_socket():

        current_time = datetime.datetime.now() 

        print("[INFO] [ {y}-{m}-{d} | {h}:{mi}:{s} ] : Creating socket...".format (
            
            y = current_time.year ,
            m = current_time.month ,
            d = current_time.day ,

            h = current_time.hour ,
            mi = current_time.minute ,
            s = current_time.second

            ) 

        )

    # Bind port and host.

    def bind_port_host( host , port ):

        current_time = datetime.datetime.now() 

        host = host

        port = port

        print ("[INFO] [ {y}-{m}-{d} | {h}:{mi}:{s} ] : Starting server on [{host}] . Port : [{port}] .".format (

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

    # Telling user that the server is ready for request.

    def ready_for_request():

        current_time = datetime.datetime.now() 

        print("[INFO] [ {y}-{m}-{d} | {h}:{mi}:{s} ] : Ready for receiving request and sending responses.".format (
            
            y = current_time.year ,
            m = current_time.month ,
            d = current_time.day ,

            h = current_time.hour ,
            mi = current_time.minute ,
            s = current_time.second

            ) 

        )

    

