import matplotlib.pyplot as plt

def plot_wave(t, y, title):
    plt.figure(figsize=(9, 3))
    plt.step(t, y, where="post", linewidth=2)
    plt.title(title)
    plt.yticks([-1, 1], ["Low", "High"])
    plt.grid(True)
    plt.show()

def nrzl(bits):
    t = list(range(len(bits) + 1))
    y = [1 if b == '1' else -1 for b in bits]
    y.append(y[-1])
    plot_wave(t, y, "NRZ-L")

def nrzi(bits):
    t = list(range(len(bits) + 1))
    y = []
    level = 1
    for b in bits:
        if b == '1':
            level *= -1
        y.append(level)
    y.append(y[-1])
    plot_wave(t, y, "NRZ-I")

def manchester(bits):
    t = [i / 2 for i in range(2 * len(bits) + 1)]
    y = []
    for b in bits:
        y += [1, -1] if b == '0' else [-1, 1]
    y.append(y[-1])
    plot_wave(t, y, "Manchester")

def diff_manchester(bits):
    t = [i / 2 for i in range(2 * len(bits) + 1)]
    y = []
    level = 1
    for b in bits:
        if b == '0':
            level *= -1
        y.append(level)
        level *= -1
        y.append(level)
    y.append(y[-1])
    plot_wave(t, y, "Differential Manchester")

while True:
    print("\n=== Line Encoding ===")
    print("1. NRZ-L")
    print("2. NRZ-I")
    print("3. Manchester")
    print("4. Differential Manchester")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "5":
        break

    bits = input("Enter binary data: ")

    if any(b not in "01" for b in bits):
        print("Invalid binary data!")
        continue

    if choice == "1":
        nrzl(bits)
    elif choice == "2":
        nrzi(bits)
    elif choice == "3":
        manchester(bits)
    elif choice == "4":
        diff_manchester(bits)
    else:
        print("Invalid choice!")