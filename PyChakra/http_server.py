#!/usr/bin/env python3

'''

    ABOUT :

    Implements a simple HTTP/1.0 Server.
    Big thanks to :

    - codementor.io 
    - geeksforgeeks.org
    
    For providing me this sample code!

'''

# Import.

import socket

# Log data.

from log_system.http_server.connect_server_log import connect_server_log_class

from log_system.http_server.run_server_log import run_server_log_class

from log_system.http_server.server_tips_log import log_tips_class

from log_system.http_server.shutdown_server_log import shutdown_server_log_class

# Import log.

log_run = run_server_log_class

log_connect = connect_server_log_class

log_tips = log_tips_class

log_shutdown = shutdown_server_log_class

# HTTP server.

def init_http_server ( 

    server_host_info , 
    server_port_info , 
    server_encoding_system ,
    server_status_info ,
    response_header , 
    response_body 

    ):
    # Info.

    log_run.start_server()

    # Log data about getting the host, port, status, response_header, and the response_body .

    log_run.getting_server_info()

    # Get the host, port, status, response_header, and the response_body .

    server_host     = server_host_info
    server_port     = server_port_info
    server_encoding = server_encoding_system
    server_status   = server_status_info
    response_header = response_header
    response_body   = response_body 

    # Log data about creating a socket object.

    log_run.create_socket()

    '''

         Create a socket object.
         AF_INET = Address - family IPv4 .
         SOCK_sTREAM = Connection-oriented TCP protocol. 

    '''

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind to the port.

    server_socket.bind( ( server_host_info , server_port_info ) ) 

    # Another log data for binding.

    log_run.bind_port_host( server_host , server_port)

    # The socket is now put into listening mode.

    server_socket.listen(5)  

    # An endless loop that will be triggered if someone decided to connect to our server.

    # Log data that remind the user that the server is ready for requests and responses.

    log_run.ready_for_request()

    print("    ")

    # Log data about CTRL + C tips.

    log_tips.run_tips()

    try:

        while True:
            
            # Establish connection with client.

            client, ( client_host, client_port ) = server_socket.accept()

            # ANOTHER LOG DATA !
            
            log_connect.beginning_connection( client_host , client_port )

            print("  ")
            
            log_connect.accept_connection( client_host , client_port )

            # ANOTHER LOG DATA !

            log_connect.send_http_status()

            # Send the HTTP version and the server status.

            send_status = "HTTP/1.0 {status}\n".format ( 

                status = server_status

            ) 
            
            send_status = bytes(send_status , encoding = server_encoding)

            client.send(send_status)

            # ANOTHER LOG DATA!

            log_connect.send_type_header()

            # Send the server response_header content type.

            send_content_type = "{content}: {contentfill}\n".format (
                
                content     = response_header[0][0] , 
                contentfill = response_header[0][1]

            )
            
            send_content_type = bytes( send_content_type , encoding = server_encoding )
            
            client.send(send_content_type)

            # ANOTHER LOG DATA !

            log_connect.send_response_body()
            
            # Send the response_body aka the HTML document.

            send_body = "{body}".format ( body = response_body )

            send_body = bytes(send_body , encoding = server_encoding_system)

            client.send ( send_body )

            # Close the connection.

            client.close()

            # ANOTHER LOG DATA !

            log_tips.run_tips()
            
    except KeyboardInterrupt:

        print("\n    ")

        # LOG DATA, WHEN THE SERVER NOTICE CTRL + C .

        log_shutdown.shutdown_notice()

        # MESSAGE, THAT SAYS " SHUTTING DOWN... "

        log_shutdown.stop_server()

        # GOOD BYE.

        log_shutdown.server_message()

        # END OF LOG DATA.

        log_shutdown.end_log_data()

        exit()

    

    


  


 





