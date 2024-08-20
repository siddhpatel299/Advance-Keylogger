import socket
import threading

# Server configuration
HOST = '198.168.0.179'  # Localhost
PORT = 12347        # Arbitrary port number

# List to keep track of connected clients and their usernames
clients = []
usernames = {}

# Function to handle incoming messages from clients
def handle_client(client_socket, addr):
    # Request and store username
    client_socket.send('Enter your username: '.encode('utf-8'))
    username = client_socket.recv(1024).decode('utf-8')
    usernames[client_socket] = username
    welcome_message = f'{username} has joined the chat!'
    print(welcome_message)
    broadcast(welcome_message.encode('utf-8'), client_socket)

    while True:
        try:
            # Receive message from a client
            message = client_socket.recv(1024).decode('utf-8')
            if message.lower() == 'exit':
                leave_message = f'{username} has left the chat.'
                print(leave_message)
                clients.remove(client_socket)
                broadcast(leave_message.encode('utf-8'), client_socket)
                client_socket.close()
                break

            formatted_message = f'{username}: {message}'
            print(formatted_message)
            # Broadcast the message to all clients
            broadcast(formatted_message.encode('utf-8'), client_socket)
        except:
            # Handle disconnection
            leave_message = f'{username} has left the chat.'
            print(leave_message)
            clients.remove(client_socket)
            broadcast(leave_message.encode('utf-8'), client_socket)
            client_socket.close()
            break

# Function to broadcast messages to all connected clients
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                # Remove client if unable to send
                clients.remove(client)
                client.close()

# Function to allow the server to send messages to all clients
def server_message():
    while True:
        msg = input('Server message: ')
        broadcast(f'SERVER: {msg}'.encode('utf-8'), None)

# Main function to start the server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f'Server started on {HOST}:{PORT}')

    # Start the server message thread
    message_thread = threading.Thread(target=server_message)
    message_thread.start()

    while True:
        # Accept new connection
        client_socket, addr = server.accept()
        print(f'Client connected from {addr}')

        # Add new client to the list
        clients.append(client_socket)

        # Start a new thread to handle the client's messages
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()

if __name__ == "__main__":
    start_server()