# Spammy Web Server

This is a simple web server written in Python, following The Programmer's Hangout guide [here](https://theprogrammershangout.com/resources/projects/http-project-guide/intro.md).

## How to use
Clone this repository and launch the server (server/sockets.py).

For Linux, open a new terminal and connect to the server with `nc -v -v localhost 14533`.
For Windows, connect to the server via a utility such as PuTTY.

## Supported Commands

- `SET <word> <definition>` - Set the definition of a word on the server
- `GET <word>` - Get a definition for a word on the server
- `DELETE <word>` - Delete a definition on the server
- `CLEAR` - Clear all definitions on the server
- `ALL` - Return all definitions stored on the server
