import socket, random

HOST, PORT = "localhost", 5000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

expected = 0
print("Receiver Started")

while True:
    try:
        data, addr = s.recvfrom(1024)
        seq = int(data.decode().split(":")[0])

        print(f"Received Frame {seq}")

        if seq == expected:
            if random.random() < 0.2:
                print("ACK Lost\n")
                continue

            s.sendto(f"ACK{seq}".encode(), addr)
            print(f"Sent ACK{seq}\n")
            expected += 1
        else:
            print("Duplicate/Out of Order")
            if expected > 0:
                s.sendto(f"ACK{expected-1}".encode(), addr)

    except:
        print("Receiver Error")