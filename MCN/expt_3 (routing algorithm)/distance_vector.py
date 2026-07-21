INF = float("inf")

try:
    V = int(input("Enter number of routers: "))
    E = int(input("Enter number of links: "))

    if V <= 0 or E < 0:
        raise ValueError

    edges = []
    print("Enter links (source destination cost):")
    for _ in range(E):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    src = int(input("Enter source router: "))
    if src < 0 or src >= V:
        raise ValueError

    dist = [INF] * V
    dist[src] = 0

    print("\nInitial Routing Table")
    print("Router\tDistance")
    for i in range(V):
        print(i, "\t", dist[i])

    for i in range(V - 1):
        print(f"\nIteration {i+1}")

        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                print(f"Updating {v}: {dist[v]} -> {dist[u] + w}")
                dist[v] = dist[u] + w

        print("Routing Table")
        print("Router\tDistance")
        for j in range(V):
            print(j, "\t", dist[j])

except:
    print("Invalid Input")