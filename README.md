# Chat Application
Here we use sockets to build a basic chat application. The application is comprised of a server side and client side, both of which have Graphical User Interfaces.

## Server
The serverGUI.py provides a basic 3x4 grid interface to take in a given IP address and ports. IP address is auto-detected, but changeable in the GUI. Then, the server will attempt to launch and bind the provided address and port and listen for connections.
The server is configured to accept up to 16 connections, and prompts all new connections for a nickname. The server will accept messages up to 1024 bytes. The server uses the broadcast() method to send the message back out to all connected clients.
![Alt text](Images/Server%20Launch.png "Server Launch GUI")<br>


## Client
The client GUI is comprised of three screens, the first screen is the client launcher, which takes in an address and port to connect and bind to.

The upon successful connection the first screen is replaced with a second screen, which serves primarily for a connection confirmation, and asks for a username.

Once a username is provided the final screen is comprised of two section, a chatbox where all messages are displayed, and below that a input box where the user can type out their next message.
This frame will accept both clicking the button to submit, and pressing the enter button to submit a message.