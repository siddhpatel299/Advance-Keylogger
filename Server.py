# import socket

# def start_server():
#     # Create a socket object
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
#     # Define server host and port
#     host = 'localhost'
#     port = 12345
    
#     # Bind the socket to the host and port
#     server_socket.bind((host, port))
    
#     # Server listens for connections (max 5 connections in the queue)
#     server_socket.listen(5)
#     print("Choose an option for attack: 1- Mouse Attack\n, 2- Restart\n, 3- keyboard monitering\n")
    
#     # Accept the client connection
#     client_socket, addr = server_socket.accept()
#     print(f"Connected to {addr}")
    
#     while True:
#         # Receive message from the client
#         client_message = client_socket.recv(1024).decode('utf-8')
#         if client_message.lower() == 'exit':
#             print("Client disconnected")
#             break
        
#         print(f"Client: {client_message}")
        
#         # Send a response back to the client
#         server_message = input("Server: ")
#         client_socket.send(server_message.encode('utf-8'))
        
#         if server_message.lower() == 'exit':
#             print("Closing connection")
#             break

#     # Close the client socket
#     client_socket.close()
#     # Close the server socket
#     server_socket.close()

# if __name__ == "__main__":
#     start_server()

import socket
import os
from _thread import * 
ServerSideSocket = socket.socket() 
host = '172.20.10.15'
port = 6000
ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e: 
    print(str(e))
    
print('Socket is listening..') 
ServerSideSocket.listen(5)
def multi_threaded_client(connection): 
    connection.send(str.encode('Server is working:')) 
    while True:
        data = connection.recv(2048).decode('utf-8') 
        print(data)
        response = input("Server :")
        if not data:
            break
    connection.sendall(str.encode(response)) 
    connection.close()
while True:
    Client, address = ServerSideSocket.accept() 
    print('Connected to: ' + address[0] + ':' + str(address[1])) 
    start_new_thread(multi_threaded_client, (Client, )) 
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()