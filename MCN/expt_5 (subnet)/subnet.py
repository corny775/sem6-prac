import ipaddress
import math

def flsm():
    try:
        net = ipaddress.IPv4Network(input("Enter Network (e.g. 192.168.1.0/24): "), strict=False)
        n = int(input("Enter number of subnets: "))
        if n <= 0:
            raise ValueError

        bits = math.ceil(math.log2(n))
        prefix = net.prefixlen + bits

        print("\nFLSM Details")
        print("-" * 45)

        for i, s in enumerate(net.subnets(new_prefix=prefix), 1):
            if i > n:
                break
            print(f"\nSubnet {i}")
            print("Network   :", s.network_address)
            print("Broadcast :", s.broadcast_address)
            print("Mask      :", s.netmask)
            print("Host Count:", s.num_addresses - 2 if s.num_addresses > 2 else 0)

    except:
        print("Invalid Input")


def vlsm():
    try:
        base = ipaddress.IPv4Network(input("Enter Base Network (e.g. 192.168.1.0/24): "), strict=False)
        n = int(input("Enter number of subnets: "))
        if n <= 0:
            raise ValueError

        req = []
        for i in range(n):
            h = int(input(f"Hosts for subnet {i+1}: "))
            req.append(h)

        req.sort(reverse=True)
        current = int(base.network_address)

        print("\nVLSM Allocation")
        print("-" * 45)

        for h in req:
            size = 1
            while size < h + 2:
                size *= 2

            prefix = 32 - int(math.log2(size))
            subnet = ipaddress.IPv4Network((current, prefix), strict=False)
            hosts = list(subnet.hosts())

            print(f"\nRequired Hosts : {h}")
            print("Network        :", subnet.network_address)
            print("Broadcast      :", subnet.broadcast_address)
            print("Mask           :", subnet.netmask)
            print("First Host     :", hosts[0] if hosts else "-")
            print("Last Host      :", hosts[-1] if hosts else "-")
            print("Host Count     :", len(hosts))

            current += subnet.num_addresses

    except:
        print("Invalid Input")


while True:
    print("\n===== Subnetting =====")
    print("1. FLSM")
    print("2. VLSM")
    print("3. Exit")

    try:
        ch = int(input("Enter choice: "))

        if ch == 1:
            flsm()
        elif ch == 2:
            vlsm()
        elif ch == 3:
            print("Program Ended")
            break
        else:
            print("Invalid Choice")

    except:
        print("Invalid Input")