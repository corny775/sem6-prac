import socket, random

HOST, PORT = "localhost", 5000
WINDOW = 4

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

base = 0
buffer = {}

print("Receiver Started")

while True:
    try:
        data, addr = s.recvfrom(1024)
        seq = int(data.decode().split(":")[0])

        print(f"Received Frame {seq}")

        if seq < base:
            s.sendto(f"ACK{seq}".encode(), addr)
            print("Duplicate\n")
            continue

        if seq < base + WINDOW:
            if seq not in buffer:
                buffer[seq] = True

            if random.random() < 0.2:
                print("ACK Lost\n")
                continue

            s.sendto(f"ACK{seq}".encode(), addr)
            print(f"Sent ACK{seq}")

            while buffer.get(base):
                del buffer[base]
                base += 1

            print("Window Base:", base, "\n")

    except:
        print("Receiver Error")