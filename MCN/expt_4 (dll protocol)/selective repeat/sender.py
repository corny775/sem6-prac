import socket, time

HOST, PORT = "localhost", 5000
WINDOW = 4
TIMEOUT = 3

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(0.5)

try:
    n = int(input("Enter number of frames: "))
    if n <= 0:
        raise ValueError

    drop = int(input("Frame to drop once (-1 for none): "))

    base = 0
    nextf = 0
    ack = [False] * n
    timer = {}
    lost = False

    print("\nSender Started")

    while base < n:

        while nextf < base + WINDOW and nextf < n:

            if nextf == drop and not lost:
                print(f"Frame {nextf} Lost")
                timer[nextf] = time.time()
                lost = True
            else:
                s.sendto(f"{nextf}:Data".encode(), (HOST, PORT))
                print(f"Sent Frame {nextf}")
                timer[nextf] = time.time()

            nextf += 1

        try:
            msg = s.recv(1024).decode()
            a = int(msg[3:])
            print("Received", msg)
            ack[a] = True

            while base < n and ack[base]:
                base += 1

        except socket.timeout:
            pass

        now = time.time()

        for i in range(base, nextf):
            if not ack[i] and now - timer.get(i, now) >= TIMEOUT:
                print(f"Timeout Frame {i}")
                s.sendto(f"{i}:Data".encode(), (HOST, PORT))
                timer[i] = now

except:
    print("Invalid Input")

s.close()