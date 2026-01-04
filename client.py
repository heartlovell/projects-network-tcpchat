import socket
import threading

# Server settings
ip = input("Enter your ip: ")
Host = ip # server address
Port = 12345        # server port


#choose a nickname

nickname = input("Choose your nickname: ")

#Create tcp socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((Host,Port))


#reciewve message from the server

def receive():
    while True:
        try:
            message = c.recv(1024).decode('utf-8')
            if message == 'NICK':
                c.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("An eror as occured")
            c.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'  # Prefix message with nickname
        c.send(message.encode('utf-8'))

# Start threads for receiving and sending messages
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()