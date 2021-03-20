#!/usr/bin/env python3

import socket
import time

# AF_INET = IPv4 address family, SOCK_STREAM = Socket type for TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(('127.0.0.1', 14533))
    sock.listen(5) # Sets max backlog number to 5
    conn, addr = sock.accept()
    
    conn.send(b"Hello Client! You are now connected to the server, prepare for some spam.")
    counter = 0
    while counter > 10:
        conn.send(b"\nSpam spam spam spam")
        counter += 1
        time.sleep(2)

    conn.close()
