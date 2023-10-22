import threading
import socket
host = '127.0.0.1'
port = 59000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()
clients = []
aliases = []

def broadcast(message,c):
    for client in clients:
        if client!=c:
            client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message,client)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} has left the chat room!'.encode(),client)
            aliases.remove(alias)
            break

def receive():
    while True:
        print('server is running and listening...')
        client, address = server.accept()
        print(f'connection is established with {address}')
        client.send('alias?'.encode())
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f'the alias of this client is {alias}')
        broadcast(f'{alias} has connected to the chat room'.encode(),client)
        client.send('you are now connected!'.encode())
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive()
