#!/usr/bin/env python3

import socket
import time

# AF_INET = IPv4 address family, SOCK_STREAM = Socket type for TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(('127.0.0.1', 14533))
    sock.listen(5) # Sets max backlog number to 5
    conn, addr = sock.accept()
    
    conn.send(b"Hello Client! You are now connected to the echo server. Type something and the server will echo it back.")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data) # Sendall blocks to ensure all data has been sent

    conn.close()
