import socket
import threading

# Define constants for server IP address and port number
SERVER_IP = 'localhost'
SERVER_PORT = 5000

# Define a class for the server thread
class ServerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = True
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((SERVER_IP, SERVER_PORT))
        self.server_socket.listen(5)
        self.clients = []

    def run(self):
        print(f"Server listening on port {SERVER_PORT}...")
        while self.running:
            client_socket, client_address = self.server_socket.accept()
            self.clients.append(client_socket)
            print(f"New client connected: {client_address}")
            client_thread = ClientThread(client_socket, self.clients)
            client_thread.start()

    def stop(self):
        self.running = False
        self.server_socket.close()

# Define a class for the client thread
class ClientThread(threading.Thread):
    def __init__(self, client_socket, clients):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.clients = clients

    def run(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if not message:
                    break
                print(f"Received message: {message}")
                for client in self.clients:
                    if client != self.client_socket:
                        client.sendall(message.encode())
            except ConnectionResetError:
                break
        self.clients.remove(self.client_socket)
        self.client_socket.close()

# Create a new server thread and start it
server_thread = ServerThread()
server_thread.start()

# Create a new client socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))
print("Connected to server.")

# Prompt the user to enter a username
username = input("Enter your username: ")

# Send the username to the server
client_socket.sendall(username.encode())

# Define a function to handle incoming messages from the server
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(message)
        except ConnectionResetError:
            break

# Start a new thread to handle incoming messages from the server
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Prompt the user to enter messages to send to the server
while True:
    message = input()
    if message == 'quit':
        break
    full_message = f"{username}: {message}"
    client_socket.sendall(full_message.encode())

# Stop the server thread and exit the program
server_thread.stop()
client_socket.close()
