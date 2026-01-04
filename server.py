import socket
import threading


#Server settings
Host = "0.0.0.0"
Port = 12345

#Create Tcp Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((Host,Port))
s.listen()
print(f"Server Strated on {Host}, {Port}")

clients = [] #Listed copnnected lcients
nicknames = [] #List store clienty connections

#Boradcast message toall clients

def broadcast(message):
    for client in clients:
        client.send(message)

#Handle invdiaual client

def handle_client(client):
    while True:
        try:
            #Recvie message fro mclient
            message = client.recv(1024)
            broadcast(message) # broadcaastting all to all the clients
        except:
            #Remove the client if th connection is lost

            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} Left the chat ".encode('utf-8'))
            nicknames.remove(nickname)
            break
        

def recieve():
    while True:
        client,addres = s.accept() #accept connection

        #Ask for nicnakme
        client.send('NICK'.encode('utf-8')) #ask client for nick name
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} joined the chat!".encode('utf-8'))
        client.send('Connected to the server!'.encode('utf-8'))


        #Start handling thread for client

        t = threading.Thread(target=handle_client,args=(client,))
        t.start()


print("Servert is running and waiting on conenctions")
recieve()
