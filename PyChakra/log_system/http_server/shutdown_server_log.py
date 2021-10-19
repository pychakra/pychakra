'''

    ABOUT THIS FILE :

    This is used to provide log data
    to http_server.py when CTRL + C
    is pressed ( aka shutdown ) .

'''

# Provide time for the log data.

import datetime 

class shutdown_server_log_class:

    # NOTICE.

    def shutdown_notice():

        current_time = datetime.datetime.now() 

        print("[INFO] [ {y}-{m}-{d} | {h}:{mi}:{s} ] : Command [CTRL + C / ^C] received. Initiating shutdown...".format (
            
            y = current_time.year ,
            m = current_time.month ,
            d = current_time.day ,

            h = current_time.hour ,
            mi = current_time.minute ,
            s = current_time.second

            ) 

        )

    # STOPPING..

    def stop_server():

        current_time = datetime.datetime.now() 

        print("[INFO] [ {y}-{m}-{d} | {h}:{mi}:{s} ] : Stopping server.".format (
            
            y = current_time.year ,
            m = current_time.month ,
            d = current_time.day ,

            h = current_time.hour ,
            mi = current_time.minute ,
            s = current_time.second

            ) 

        )

    # FINAL MESSAGE...

    def server_message():

        current_time = datetime.datetime.now() 

        print("[INFO] [ {y}-{m}-{d} | {h}:{mi}:{s} ] : Goodbye...".format (
            
            y = current_time.year ,
            m = current_time.month ,
            d = current_time.day ,

            h = current_time.hour ,
            mi = current_time.minute ,
            s = current_time.second

            ) 

        )

    # END OF LOG DATA...

    def end_log_data():

        current_time = datetime.datetime.now() 

        print("   ")
        
        print("END OF LOG DATA . TIME : [ {y}-{mi}-{d} | {h}:{m}:{s} ] .".format (

            y = current_time.year ,
            m = current_time.month ,
            d = current_time.day ,

            h = current_time.hour ,
            mi = current_time.minute ,
            s = current_time.second

            )

        )

        print("   ")

