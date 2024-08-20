import socket
import threading

# Server configuration (same as server)
HOST = '198.168.0.179'
PORT = 12347

# Function to handle receiving messages from the server
def receive_messages(client_socket):
    while True:
        try:
            # Receive and print messages from the server
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
        except:
            # Close connection on error
            print('Connection closed by the server.')
            client_socket.close()
            break

# Function to start the client
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # Start a thread to handle incoming messages from the server
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # Send username to the server
    username = input('Enter your username: ')
    client_socket.send(username.encode('utf-8'))

    # Handle sending messages to the server
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))
        if message.lower() == 'exit':
            print('You have exited the chat.')
            client_socket.close()
            break

if __name__ == "__main__":
    start_client()