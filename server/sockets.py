#!/usr/bin/env python3

import socket

# GET a definition from the dictionary
def get_defition(reply_split):
    arg = reply_split[1] # Will only return the first definition if multiple are passed
    if arg in defs.keys():
        definition = str(defs[arg])
        # Respond to the client with the definition
        def_bytes = bytes(definition, "UTF-8")
        reply = b"".join([b"\nDefinition:\n", def_bytes, b"\n\n"])
        conn.sendall(reply)
    else:
        # Defitinion not found
        conn.send(b"\nERROR undefined.\n")


# SET a new defition in the dictionary
def set_defition(reply_split):
    # Format is <command> <word> <def (multiple words)>
    word = reply_split[1]
    defs[word] = " ".join(reply_split[2:])
    conn.send(b"\nDefinition created in dictionary.\n\n")


# DELETE a single definition in the dictionary
def delete_definition(reply_split):
    word = reply_split[1]
    if word in defs.keys():
        del defs[word]
        reply = bytes("{} deleted from dictionary\n\n".format(word), "UTF-8")
        conn.send(reply)
    else:
        conn.send(b"ERROR word undefined.")


# CLEAR all definitions in the dictionary
def clear_definitions():
    length = len(defs)
    defs.clear()
    reply = "\n{} definitions cleared.\n\n".format(length)
    conn.send(bytes(reply, "UTF-8")) 


# GET ALL definitions from the dictionary
def all_definitions():
    # String all definitions together and send as one string
    reply = ""
    for key in defs:
        definition = "\n{}: {}\n".format(key, defs[key])
        reply.join(definition)
    reply.join("\n\n")
    conn.sendall(bytes(reply, "UTF-8"))


# AF_INET = IPv4 address family, SOCK_STREAM = Socket type for TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    print("Booting server...")
    sock.bind(('127.0.0.1', 14533))
    sock.listen(5) # Sets max backlog number to 5
    conn, addr = sock.accept()
    
    conn.send(b"Connected to definitions server.\n")
    print("Client connected to server at 127.0.0.1:14533")
    defs = dict()
    while True:
        reply = conn.recv(1024)
        if not reply:
            break

        # Parse the response and obtain arguments
        reply_str = reply.decode("UTF-8")
        reply_split = reply_str.split()
        command = reply_split[0].upper()

        if command == "GET" and len(reply_split) >= 2:
            get_defition(reply_split)
        elif command.upper() == "SET" and len(reply_split) >= 3:
            set_defition(reply_split)
        elif command.upper() == "DELETE" and len(reply_split) >= 2:
            delete_definition(reply_split)
        elif command.upper() == "CLEAR":
            clear_definitions()
        elif command.upper() == "ALL":
            all_definitions()
        else:
            conn.send(b"\nERROR command undefined.\n")


    conn.close()
