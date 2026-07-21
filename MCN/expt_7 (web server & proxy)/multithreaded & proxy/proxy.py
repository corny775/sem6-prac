import socket
import threading

HOST, PORT = "localhost", 8888
BUFFER = 4096

def handle_client(client):
    try:
        request = client.recv(BUFFER)
        if not request:
            return

        print("\n----- HTTP Request -----")
        print(request.decode(errors="ignore"))

        text = request.decode(errors="ignore")
        host = ""

        for line in text.split("\n"):
            if line.lower().startswith("host:"):
                host = line.split(":", 1)[1].strip().split(":")[0]
                break

        if not host:
            return

        print("Forwarding to:", host)

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect((host, 80))
        server.sendall(request)

        while True:
            data = server.recv(BUFFER)
            if not data:
                break
            client.sendall(data)

        server.close()

    except Exception as e:
        print("Error:", e)

    finally:
        client.close()

proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxy.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
proxy.bind((HOST, PORT))
proxy.listen(5)

print(f"Proxy Server running on {HOST}:{PORT}")

while True:
    client, addr = proxy.accept()
    print("Client Connected:", addr)
    threading.Thread(target=handle_client, args=(client,)).start()