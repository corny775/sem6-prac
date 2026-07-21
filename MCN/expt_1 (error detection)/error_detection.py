def parity():
    d = input("Data bits: ")
    p = d.count("1") % 2
    print("Parity Bit:", p)
    print("Transmitted:", d + str(p))

def block_parity():
    r = int(input("Rows: "))
    c = int(input("Cols: "))
    d = input(f"Enter {r*c} bits: ")

    mat = [list(map(int, d[i*c:(i+1)*c])) for i in range(r)]
    rp = [sum(row) % 2 for row in mat]
    cp = [sum(mat[i][j] for i in range(r)) % 2 for j in range(c)]

    print("Row Parity:", rp)
    print("Column Parity:", cp)

def crc():
    data = input("Data bits: ")
    gen = input("Generator bits: ")

    div = list(data + "0"*(len(gen)-1))

    for i in range(len(data)):
        if div[i] == "1":
            for j in range(len(gen)):
                div[i+j] = str(int(div[i+j]) ^ int(gen[j]))

    rem = "".join(div)[-(len(gen)-1):]
    print("CRC:", rem)
    print("Codeword:", data + rem)

def checksum():
    nums = list(map(int, input("Numbers: ").split()))
    s = sum(nums)
    cs = ~s & 255
    print("Checksum:", cs)

def hamming():
    d = list(map(int, input("4 bits: ").split()))

    p1 = d[0]^d[1]^d[3]
    p2 = d[0]^d[2]^d[3]
    p4 = d[1]^d[2]^d[3]

    print("Hamming Code:", p1,p2,d[0],p4,d[1],d[2],d[3])

while True:
    print("\n1. Parity")
    print("2. Block Parity")
    print("3. CRC")
    print("4. Checksum")
    print("5. Hamming Code")
    print("6. Exit")

    try:
        ch = int(input("Choice: "))

        if ch == 1:
            parity()
        elif ch == 2:
            block_parity()
        elif ch == 3:
            crc()
        elif ch == 4:
            checksum()
        elif ch == 5:
            hamming()
        elif ch == 6:
            print("Thank You")
            break
        else:
            print("Invalid Choice")

    except Exception:
        print("Invalid Input")