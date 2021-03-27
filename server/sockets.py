#!/usr/bin/env python3

import socket

# AF_INET = IPv4 address family, SOCK_STREAM = Socket type for TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(('127.0.0.1', 14533))
    sock.listen(5) # Sets max backlog number to 5
    conn, addr = sock.accept()
    
    conn.send(b"Hello Client! You are now connected to the dictionary server. Add or search for a definition.\n")
    defs = dict()
    defs["def"] = "Hello, this is a test definition! If you are seeing this, then the protocol works!"
    while True:
        reply = conn.recv(1024)
        if not reply:
            break

        # Parse the response and obtain arguments
        reply_str = reply.decode("UTF-8")
        reply_split = reply_str.split()
        command, arg = None, None

        if len(reply_split) >= 2:
            command = reply_split[0]
            arg = reply_split[1]
            if command.upper() == "GET":
                if arg in defs.keys():
                    definition = str(defs[arg])
                    # Respond to the client again
                    conn.send(b"\nDefinition:\n") 
                    conn.sendall(bytes(definition, "UTF-8"))
                    conn.send(b"\n\n")
                else:
                    conn.send(b"\nERROR - Definition not found.\n")
            else:
                conn.send(b"\nERROR - Command not supported.\n")
        else: 
            conn.send(b"\nERROR - Not enough arguments given - requred in format 'VERB <argument>'\n")

    conn.close()
