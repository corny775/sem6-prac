import socket, random

HOST, PORT = "localhost", 5000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

expected = 0
print("Receiver Started...")

while True:
    try:
        data, addr = s.recvfrom(1024)
        frame = data.decode()

        seq, msg = frame.split(":", 1)
        seq = int(seq)

        print(f"\nReceived -> {frame}")

        if seq == expected:
            print("Accepted:", msg)

            if random.random() < 0.2:
                print("ACK Lost!")
                continue

            ack = f"ACK{seq}"
            s.sendto(ack.encode(), addr)
            print("Sent ->", ack)
            expected = 1 - expected

        else:
            print("Duplicate Frame")
            s.sendto(f"ACK{1-expected}".encode(), addr)

    except:
        print("Receiver Error")