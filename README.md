# 🐍 🖥 Python TCP Chat Room
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

## Sockets
Sockets and the socket API are used to send messages across a network. They provide a form of inter-process communication (IPC). The network can be a logical, local network to the computer, or one that’s physically connected to an external network, with its own connections to other networks. The obvious example is the Internet, which you connect to via your ISP.

<img src="https://github.com/user-attachments/assets/1f6bcbae-c782-4d4f-a04e-7a396006de1c" width="300" />
Image Credit:Real Python


## TCP Socket
In the diagram below, given the sequence of socket API calls and data flow for TCP:
<img src="https://github.com/user-attachments/assets/1f6bcbae-c782-4d4f-a04e-7a396006de1c" width="300" height="338" />



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



If a client disconnects → server detects → removes the client → bro
