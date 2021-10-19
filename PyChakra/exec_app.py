'''

    ABOUT THIS FILE :

    In order to avoid Circular Import error,
    instead of running application() right
    in init_server.py..  which causes circular
    import, Im going to execute application()
    on this file. All the data needed are send
    from init_server.py to this file.

'''

from log_system.start_server import exec_app_log

'''

    This variable represents a class called exec_app_log_class
    at file exec_app_log .

'''

log = exec_app_log.exec_app_log_class

# run_app()

def run_app(environ , host , port , app , encoding ):

    # Import start_response .

    from start_response import start_response

    from start_response import pass_host_port_encoding

    start_response = start_response

    # Transport all the data.

    environ        = environ
    host           = host
    port           = port
    start_response = start_response
    encoding       = encoding

    # Log data for executing function trans_host_port() .

    log.exec_pass_host_port_encoding()

    # Execute function trans_host_port() .

    pass_host_port_encoding ( host , port , encoding )

    # Log data for executing function application() .

    log.exec_application()

    '''

       Execute application(), this was done in this file
       in order to avoid circular import error.

    '''

    app ( environ, start_response )
