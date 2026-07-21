def char_count():
    data = input("Enter data: ")
    size = int(input("Frame size: "))

    print("Frames:")
    for i in range(0, len(data), size):
        frame = data[i:i+size]
        print(f"{len(frame)+1}{frame}")

def byte_stuff():
    data = input("Enter data: ")
    stuffed = ""

    for ch in data:
        if ch in ['F', 'E']:
            stuffed += 'E'
        stuffed += ch

    print("Framed Data: F" + stuffed + "F")

def bit_stuff():
    data = input("Enter binary data: ")
    stuffed = ""
    count = 0

    for bit in data:
        stuffed += bit
        if bit == '1':
            count += 1
            if count == 5:
                stuffed += '0'
                count = 0
        else:
            count = 0

    print("Framed Data: 01111110", stuffed, "01111110")

while True:
    print("\n1. Character Count")
    print("2. Byte Stuffing")
    print("3. Bit Stuffing")
    print("4. Exit")

    try:
        ch = int(input("Choice: "))

        if ch == 1:
            char_count()
        elif ch == 2:
            byte_stuff()
        elif ch == 3:
            bit_stuff()
        elif ch == 4:
            print("Thank You")
            break
        else:
            print("Invalid Choice")

    except:
        print("Invalid Input")