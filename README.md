🖥 Python TCP Chat

A multi-client chat application built in Python using TCP sockets.
Clients can connect to the server, pick a nickname, and chat in real-time. This project demonstrates TCP/IP networking, client-server architecture, multithreading, and network debugging.

About This Project

This project was created to explore the fundamentals of network programming. It highlights:

How a TCP server can manage multiple client connections concurrently.

How clients can send and receive messages in real-time.

How to implement error handling to manage client disconnects gracefully.

Skills in Python socket programming and threaded programming.

How the Chat Works
Component	Description
Server	Listens for client connections, asks for a nickname, and broadcasts messages to all connected clients. Uses threads to handle each client separately.
Client	Connects to the server, sends the nickname, and can send/receive messages. Uses two threads: one for sending and one for receiving messages to avoid blocking.
Networking	Uses TCP sockets (SOCK_STREAM) for reliable communication. The server binds to a host and port, while clients connect to that address.
Multithreading	Each client runs in its own thread on the server, so multiple clients can chat simultaneously.
Error Handling	The server detects when a client disconnects unexpectedly, removes it from the list, and broadcasts a "left the chat" message.
Key Features

Multi-client support: Multiple clients can chat at the same time.

Nickname management: Each client chooses a nickname at connection.

Message broadcasting: Every message is sent to all connected clients.

Threading: Server uses threads for concurrent client handling; clients use threads for simultaneous sending/receiving.

Error handling: Detects client disconnects and network errors (e.g., WinError 10049).

Technical Details
Server Workflow

Create a TCP socket and bind it to a host and port.

Listen for incoming client connections.

When a client connects:

Ask for a nickname.

Add the client socket and nickname to tracking lists.

Broadcast a "joined the chat" message.

Start a new thread to handle this client’s messages.

Each client thread:

Receives messages from the client.

Broadcasts messages to all other clients.

Handles disconnects by removing the client and broadcasting a "left the chat" message.

Client Workflow

Connect to the server using the server's host and port.

Send nickname when prompted.

Run two threads:

Receive thread: Continuously receives messages from the server and prints them.

Write thread: Takes user input and sends it to the server.

Skills Demonstrated

TCP/IP socket programming in Python.

Client-server architecture design.

Multithreading for concurrent connections.

Network debugging and handling disconnects (WinError 10049).

Building a real-time interactive application.

Example Output / Screenshots

Add screenshots or GIFs of your chat application running:


Example of two clients chatting in real-time.
