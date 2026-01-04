# 🖥 Python TCP Chat
**A multi-client chat application built with Python using TCP sockets.**  
Clients can connect, pick a nickname, and chat in real-time. Demonstrates **TCP/IP networking, multithreading, and network debugging**.

---

## About This Project
This repository showcases my **Python TCP chat project**, focusing on practical applications of **network protocols, socket programming, and client-server communication**. This project highlights my ability to **design, implement, and debug network applications**, handle multiple clients concurrently, and manage real-time messaging.

---

## Project Details

| Project | Description | Key Technologies |
|---------|-------------|----------------|
| **Python TCP Chat** | Multi-client chat application with nickname management, real-time messaging, and handling client disconnects gracefully. Solved networking issues like `WinError 10049`. | Python, socket, threading, TCP/IP |

---

## Features

- Multi-client chat support  
- Nickname registration for each client  
- Real-time message broadcasting to all connected clients  
- Threaded server for handling multiple clients simultaneously  
- Graceful error handling and client disconnect detection  

---

## Skills Demonstrated

- TCP/IP socket programming in Python  
- Client-server architecture  
- Multithreading for concurrent client connections  
- Network debugging (e.g., WinError 10049)  
- Real-time messaging application design  

---

## Screenshots / GIFs

> Add images or GIFs to showcase your chat application. Replace the placeholders with your screenshots.

![Python TCP Chat](screenshots/chat.png)  
*Python TCP Chat running with multiple clients.*

---

## How to Run

1. **Clone the repository:**  
```bash
git clone https://github.com/yourusername/projects-network-tcpchat.git
```

## Detailed Explanation

This section explains in detail how the **Python TCP chat application works**, including the server and client workflows, message flow, and threading.

---

### Server Workflow

#### 1. Socket Creation

```python
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen()
bind() assigns the server to a specific IP address and port.

listen() puts the server in listening mode, waiting for incoming client connections.

3. Accepting Clients
python
Copy code
client, address = server.accept()
Blocks execution until a client connects.

Returns a socket object for communication and the client’s IP address.

4. Nickname Handling
python
Copy code
client.send('NICK'.encode('utf-8'))
nickname = client.recv(1024).decode('utf-8')
Server asks the client to send a nickname.

Stores the nickname in a list to keep track of connected clients.

5. Threaded Client Handling
python
Copy code
thread = threading.Thread(target=handle_client, args=(client,))
thread.start()
Each client runs in a dedicated thread, allowing multiple clients to chat simultaneously without blocking each other.

6. Broadcasting Messages
python
Copy code
def broadcast(message):
    for client in clients:
        client.send(message)
Sends a message to all connected clients.

Used for chat messages, join notifications, and leave notifications.

7. Handling Disconnects
python
Copy code
except:
    index = clients.index(client)
    clients.remove(client)
    client.close()
    nickname = nicknames[index]
    broadcast(f"{nickname} left the chat!".encode('utf-8'))
    nicknames.remove(nickname)
Detects if a client disconnects unexpectedly.

Removes the client and nickname from tracking lists.

Notifies other clients that someone left the chat.

Client Workflow
1. Socket Creation and Connection
python
Copy code
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
Connects to the server using the server’s IP and port.

2. Sending Nickname
python
Copy code
if message == 'NICK':
    client.send(nickname.encode('utf-8'))
Sends the nickname to the server when prompted.

3. Receiving Messages (Threaded)
python
Copy code
def receive():
    while True:
        message = client.recv(1024).decode('utf-8')
        print(message)
Continuously listens for messages from the server.

Runs in a separate thread so it does not block user input.

4. Sending Messages (Threaded)
python
Copy code
def write():
    while True:
        message = f"{nickname}: {input('')}"
        client.send(message.encode('utf-8'))
Takes input from the user and sends it to the server.

Runs in a separate thread to allow simultaneous sending and receiving.

How Messages Flow
Client types a message → sends it to the server.

Server receives the message → calls broadcast() → sends the message to all connected clients.

All clients receive the message → display it in real-time.

If a client disconnects → server detects → removes the client → bro
