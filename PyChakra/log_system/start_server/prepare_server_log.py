'''

    ABOUT THIS FILE :

    This is used to provide log data
    to init_server.py .

'''

# Provide time for the log data.

import datetime 
class init_server_log_class:

    # ABOUT.

    def about():

        current_time = datetime.datetime.now() 

        print("   ")

        print("ABOUT :")

        print("   ")

        print("PyChakra Version [0.3.0] - Release [Stable] .")
        print("Licensed in GNU Public License 3 ( GPL 3 ) .")
        print("Developed and Published by [PyChakra Team] .")
        print("Website : [https://pychakra.github.io] .")

        print("   ")

    # BEGINNING.

    def beginning():

        current_time = datetime.datetime.now() 

        print("BEGINNING OF LOG DATA . TIME : [ {y}-{m}-{d} | {h}:{mi}:{s} ] :".format (

            y = current_time.year ,
            m = current_time.month ,
            d = current_time.day ,

            h = current_time.hour ,
            mi = current_time.minute ,
            s = current_time.second

            ) 
        
        )

        print("   ")
    
    # Execute run server.

    def exec_run_server():

        current_time = datetime.datetime.now() 

        print ("[INFO] [ {y}-{m}-{d} | {h}:{mi}:{s} ] : Executing function [run_server] from file [init_server.py] .".format (

            y = current_time.year ,
            m = current_time.month ,
            d = current_time.day ,

            h  = current_time.hour ,
            mi = current_time.minute ,
            s  = current_time.second

            ) 

        )

    def exec_run_app():

        current_time = datetime.datetime.now() 

        print ("[INFO] [ {y}-{m}-{d} | {h}:{mi}:{s} ] : Executing function [run_app] from file [exec_app.py] .".format (

            y = current_time.year ,
            m = current_time.month ,
            d = current_time.day ,

            h  = current_time.hour ,
            mi = current_time.minute ,
            s  = current_time.second

            ) 

        )  