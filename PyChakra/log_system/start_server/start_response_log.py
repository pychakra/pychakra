'''

    ABOUT THIS FILE :

    This is used to provide log data
    to start_response.py .

'''

# Provide time for the log data.

import datetime 

class start_response_log_class:

    # Execute start_response() .

    def exec_start_response():

        current_time = datetime.datetime.now() 

        print("[INFO] [ {y}-{m}-{d} | {h}:{mi}:{s} ] : Executing function [start_response] from file [start_response.py] .".format (

            y = current_time.year ,
            m = current_time.month ,
            d = current_time.day ,

            h = current_time.hour ,
            mi = current_time.minute ,
            s = current_time.second

            ) 

        )

    # Execute init_http_server() .

    def exec_init_http_server():

        current_time = datetime.datetime.now() 

        print("[INFO] [ {y}-{m}-{d} | {h}:{mi}:{s} ] : Executing function [init_http_server] from file [http_server.py] .".format (

            y = current_time.year ,
            m = current_time.month ,
            d = current_time.day ,

            h = current_time.hour ,
            mi = current_time.minute ,
            s = current_time.second

            ) 

    )
    
