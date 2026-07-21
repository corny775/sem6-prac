import socket

HOST, PORT = "localhost", 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Waiting for client...")
conn, addr = server.accept()
print("Connected:", addr)

while True:
    msg = conn.recv(1024).decode()

    if not msg or msg.lower() == "exit":
        print("Client disconnected.")
        break

    print("Client:", msg)

    reply = input("Server: ")
    conn.send(reply.encode())

    if reply.lower() == "exit":
        break

conn.close()
server.close()