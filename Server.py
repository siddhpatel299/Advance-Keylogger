# # import socket

# # def start_server():
# #     # Create a socket object
# #     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
# #     # Define server host and port
# #     host = 'localhost'
# #     port = 12345
    
# #     # Bind the socket to the host and port
# #     server_socket.bind((host, port))
    
# #     # Server listens for connections (max 5 connections in the queue)
# #     server_socket.listen(5)
# #     print("Choose an option for attack: 1- Mouse Attack\n, 2- Restart\n, 3- keyboard monitering\n")
    
# #     # Accept the client connection
# #     client_socket, addr = server_socket.accept()
# #     print(f"Connected to {addr}")
    
# #     while True:
# #         # Receive message from the client
# #         client_message = client_socket.recv(1024).decode('utf-8')
# #         if client_message.lower() == 'exit':
# #             print("Client disconnected")
# #             break
        
# #         print(f"Client: {client_message}")
        
# #         # Send a response back to the client
# #         server_message = input("Server: ")
# #         client_socket.send(server_message.encode('utf-8'))
        
# #         if server_message.lower() == 'exit':
# #             print("Closing connection")
# #             break

# #     # Close the client socket
# #     client_socket.close()
# #     # Close the server socket
# #     server_socket.close()

# # if __name__ == "__main__":
# #     start_server()

# import socket
# import os
# from _thread import * 
# ServerSideSocket = socket.socket() 
# host = '172.20.10.15'
# port = 6001
# ThreadCount = 0
# try:
#     ServerSideSocket.bind((host, port))
# except socket.error as e: 
#     print(str(e))
    
# print('Socket is listening..') 
# ServerSideSocket.listen(5)
# def multi_threaded_client(connection): 
#     connection.send(str.encode('Server is working:')) 
#     while True:
#         data = connection.recv(2048).decode('utf-8') 
#         print(data)
#         response = input("Server :")
#         if not data:
#             break
#     connection.sendall(str.encode(response)) 
#     connection.close()
# while True:
#     Client, address = ServerSideSocket.accept() 
#     print('Connected to: ' + address[0] + ':' + str(address[1])) 
#     start_new_thread(multi_threaded_client, (Client, )) 
#     ThreadCount += 1
#     print('Thread Number: ' + str(ThreadCount))
# ServerSideSocket.close()

# Python program to implement server side of chat room. 
import socket 
import select 
import sys 
'''Replace "thread" with "_thread" for python 3'''
from _thread import *

"""The first argument AF_INET is the address domain of the 
socket. This is used when we have an Internet Domain with 
any two hosts The second argument is the type of socket. 
SOCK_STREAM means that data or characters are read in 
a continuous flow."""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

# checks whether sufficient arguments have been provided 
# if len(sys.argv) != 3: 
# 	print ("Correct usage: script, IP address, port number")
# 	exit() 

# takes the first argument from command prompt as IP address 
IP_address = '10.159.134.117'

# takes second argument from command prompt as port number 
Port = 6005 

""" 
binds the server to an entered IP address and at the 
specified port number. 
The client must be aware of these parameters 
"""
server.bind((IP_address, Port)) 

""" 
listens for 100 active connections. This number can be 
increased as per convenience. 
"""
server.listen(100) 

list_of_clients = [] 

def clientthread(conn, addr): 

	# sends a message to the client whose user object is conn 
	conn.send("Welcome to this chatroom!") 

	while True: 
			try: 
				message = conn.recv(2048) 
				if message: 

					"""prints the message and address of the 
					user who just sent the message on the server 
					terminal"""
					print ("<" + addr[0] + "> " + message) 

					# Calls broadcast function to send message to all 
					message_to_send = "<" + addr[0] + "> " + message 
					broadcast(message_to_send, conn) 

				else: 
					"""message may have no content if the connection 
					is broken, in this case we remove the connection"""
					remove(conn) 

			except: 
				continue

"""Using the below function, we broadcast the message to all 
clients who's object is not the same as the one sending 
the message """
def broadcast(message, connection): 
	for clients in list_of_clients: 
		if clients!=connection: 
			try: 
				clients.send(message) 
			except: 
				clients.close() 

				# if the link is broken, we remove the client 
				remove(clients) 

"""The following function simply removes the object 
from the list that was created at the beginning of 
the program"""
def remove(connection): 
	if connection in list_of_clients: 
		list_of_clients.remove(connection) 

while True: 

	"""Accepts a connection request and stores two parameters, 
	conn which is a socket object for that user, and addr 
	which contains the IP address of the client that just 
	connected"""
	conn, addr = server.accept() 

	"""Maintains a list of clients for ease of broadcasting 
	a message to all available people in the chatroom"""
	list_of_clients.append(conn) 

	# prints the address of the user that just connected 
	print (addr[0] + " connected")

	# creates and individual thread for every user 
	# that connects 
	start_new_thread(clientthread,(conn,addr))	 

conn.close() 
server.close() 
