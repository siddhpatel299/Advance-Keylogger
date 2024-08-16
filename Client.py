import socket

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define server IP address and port
    host = 'localhost'
    port = 12345
    
    # Connect to the server
    client_socket.connect((host, port))
    
    while True:
        
        # Send a message to the server
        client_message = input("Client: ")
        client_socket.send(client_message.encode('utf-8'))
        
        if client_message.lower() == 'exit':
            print("Closing connection")
            break
        
        # Receive response from the server
        server_message = client_socket.recv(1024).decode('utf-8')
        if server_message.lower() == 'exit':
            print("Server closed the connection")
            break
        
        print(f"Server: {server_message}")

    # Close the client socket
    client_socket.close()

if __name__ == "__main__":
    start_client()
