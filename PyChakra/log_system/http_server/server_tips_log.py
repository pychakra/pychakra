'''

    ABOUT THIS FILE :

    This is used to provide log data
    to http_server .

'''

# Provide time for the log data.

import datetime 

class log_tips_class:

    # CTRL + C tip.

    def run_tips():

        current_time = datetime.datetime.now() 

        print("[TIPS] [ {y}-{m}-{d} | {h}:{mi}:{s} ] : Press [CTRL + C] to stop the server.".format (
            
            y = current_time.year ,
            m = current_time.month ,
            d = current_time.day ,

            h = current_time.hour ,
            mi = current_time.minute ,
            s = current_time.second

            ) 

        )

        print("    ")