'''

    ABOUT THIS FILE :

    This is used to provide log data
    to exec_app.py .

'''

# Provide time for the log data.

import datetime 

class exec_app_log_class:

    # Log for passing host, port, and encoding method.

    def exec_pass_host_port_encoding():

        current_time = datetime.datetime.now() 

        print ("[INFO] [ {y}-{m}-{d} | {h}:{mi}:{s} ] : Executing function [pass_host_port_encoding] from file [start_response.py] .".format (

            y = current_time.year ,
            m = current_time.month ,
            d = current_time.day ,

            h = current_time.hour ,
            mi = current_time.minute ,
            s = current_time.second

            ) 

        )

    # Execute application.

    def exec_application():

        current_time = datetime.datetime.now() 

        print ("[INFO] [ {y}-{m}-{d} | {h}:{mi}:{s} ] : Executing function [application] from file [app.py] .".format (

            y = current_time.year ,
            m = current_time.month ,
            d = current_time.day ,

            h = current_time.hour ,
            mi = current_time.minute ,
            s = current_time.second

            ) 

        )