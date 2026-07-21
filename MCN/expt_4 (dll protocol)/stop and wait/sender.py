import socket

HOST, PORT = "localhost", 5000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(3)

seq = 0

print("Sender Started...")

while True:
    msg = input("\nMessage (exit to quit): ")

    if msg.lower() == "exit":
        break

    while True:

        if msg.lower() == "drop":
            print("Frame Lost (Simulation)")
            msg = input("Enter message again: ")
            continue

        frame = f"{seq}:{msg}"

        try:
            print("Sending ->", frame)
            s.sendto(frame.encode(), (HOST, PORT))

            ack, _ = s.recvfrom(1024)
            ack = ack.decode()

            if ack == f"ACK{seq}":
                print("Received ->", ack)
                seq = 1 - seq
                break
            else:
                print("Wrong ACK")

        except socket.timeout:
            print("Timeout! Retransmitting...")

        except:
            print("Sender Error")