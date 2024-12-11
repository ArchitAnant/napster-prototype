import socket
import time

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a server
server_address = (input("Enter server ip: "), int(input("Enter port no.: ")))  

count= 0

if count<10:
# Send data
    client_socket.connect(server_address)

    res = client_socket.recv(1024)
    print("Server resp:",res.decode())
    mess = "69"
    client_socket.sendall(mess.encode())
    while True:
        try:
            res = client_socket.recv(1024)
            if len(res.decode())!=0:
                print("Server resp:",res.decode())
        except KeyboardInterrupt:
            print("Exiting")
            break
        except:
            continue

    # Close the connection
    client_socket.close()
else:
    print("Server not reachable!")
