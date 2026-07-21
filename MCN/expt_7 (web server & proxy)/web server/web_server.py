import socket
import os

HOST, PORT = "localhost", 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Web Server running at http://{HOST}:{PORT}")

while True:
    conn, addr = server.accept()
    print("\nConnected:", addr)

    try:
        request = conn.recv(1024).decode()
        print("\nHTTP Request:\n")
        print(request)

        file = request.split()[1].lstrip("/")
        if file == "":
            file = "index.html"

        with open(file, "rb") as f:
            data = f.read()

        header = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n"
            f"Content-Length: {len(data)}\r\n\r\n"
        )

        conn.send(header.encode())
        conn.send(data)

    except FileNotFoundError:
        html = "<h1>404 Not Found</h1>"
        header = (
            "HTTP/1.1 404 Not Found\r\n"
            "Content-Type: text/html\r\n\r\n"
        )
        conn.send(header.encode() + html.encode())

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()