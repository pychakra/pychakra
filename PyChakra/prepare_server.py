#!/usr/bin/env python3

'''

    PyChakra Version [0.3.0] - Release [Stable] .
    Licensed in GNU Public License 3 ( GPL 3 ) .
    Website : [https://pychakra.github.io] .  
    Developed and Published by [PyChakra Team] .

'''

'''

    ABOUT THIS FILE :

    This file will execute the application
    function in the app.py , app.py is going
    to trigger a function call send_response()
    that will force run_start_response.py to
    send all the data to the http_server.py .

'''

# Import.

import os

import exec_app 

from log_system.start_server import prepare_server_log

'''

    This variable represents a class called init_server_log_class
    at file init_server_log .

'''

log = prepare_server_log.init_server_log_class

# File : exec_app .

exec_app = exec_app

# Execute application.

def run_server( host , port , app , encoding ) :

    # Telling user about PyChakra.

    log.about()

    # Log data for telling user the beginning of log data.

    log.beginning()

    # Log data for executing function run_server() .

    log.exec_run_server()

    host     = host
    port     = port
    encoding = encoding

    # Log data for executing function run_app() .

    log.exec_run_app()

    # Execute run_app() .

    exec_app.run_app ( os.environ , host , port , app , encoding)

