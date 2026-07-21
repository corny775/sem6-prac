import socket

HOST, PORT = "localhost", 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Connected to server.")

while True:
    msg = input("Client: ")
    client.send(msg.encode())

    if msg.lower() == "exit":
        break

    reply = client.recv(1024).decode()

    if not reply or reply.lower() == "exit":
        print("Server disconnected.")
        break

    print("Server:", reply)

client.close()