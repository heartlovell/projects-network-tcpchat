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
```
bind() assigns the server to a specific IP address and port.

listen() puts the server in listening mode, waiting for incoming client connections.


# Accepting Clients
```python
client, address = server.accept()
```
Blocks execution until a client connects.

Returns a socket object for communication and the client’s IP address.


If a client disconnects → server detects → removes the client → bro
