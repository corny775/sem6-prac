INF = float("inf")

try:
    n = int(input("Enter number of routers: "))
    if n <= 0:
        raise ValueError

    graph = [list(map(int, input().split())) for _ in range(n)]

    src = int(input("Enter source router: "))
    if src < 0 or src >= n:
        raise ValueError

    dist = graph[src][:]
    visited = [False] * n
    dist[src] = 0
    visited[src] = True

    print("\nInitial Routing Table")
    print("Router\tDistance")
    for i in range(n):
        print(i, "\t", dist[i])

    for step in range(n - 1):
        m = INF
        u = -1

        for i in range(n):
            if not visited[i] and dist[i] < m:
                m = dist[i]
                u = i

        if u == -1:
            break

        visited[u] = True
        print(f"\nProcessing Router {u}")

        for v in range(n):
            if not visited[v] and graph[u][v] != 9999:
                if dist[u] + graph[u][v] < dist[v]:
                    print(f"Updating {v}: {dist[v]} -> {dist[u] + graph[u][v]}")
                    dist[v] = dist[u] + graph[u][v]

        print("Routing Table")
        print("Router\tDistance")
        for i in range(n):
            print(i, "\t", dist[i])

except:
    print("Invalid Input")