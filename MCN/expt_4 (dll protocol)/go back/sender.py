import socket

HOST, PORT = "localhost", 5000
WINDOW = 4

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(3)

try:
    n = int(input("Enter number of frames: "))
    if n <= 0:
        raise ValueError

    base = 0
    nextf = 0
    lost = set()

    print("\nType frame number to drop once (-1 for none)")
    drop = int(input("Frame to drop: "))

    while base < n:

        while nextf < base + WINDOW and nextf < n:

            if nextf == drop and nextf not in lost:
                print(f"Frame {nextf} Lost")
                lost.add(nextf)
            else:
                s.sendto(f"{nextf}:Data".encode(), (HOST, PORT))
                print(f"Sent Frame {nextf}")

            nextf += 1

        try:
            ack = s.recv(1024).decode()
            a = int(ack[3:])

            print("Received", ack)

            if a >= base:
                base = a + 1

        except socket.timeout:
            print("Timeout! Go Back")
            nextf = base

except:
    print("Invalid Input")

s.close()