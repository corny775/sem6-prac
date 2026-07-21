from collections import deque

def bfs(graph, start):
    visited = [start]
    queue = deque([start])

    while queue:
        u = queue.popleft()
        print(u, end=" ")
        for v in graph[u]:
            if v not in visited:
                visited.append(v)
                queue.append(v)

n = int(input("Enter no of nodes: "))
graph = {}

for i in range(n):
    v = input(f"Enter vertex {i+1}: ")
    graph[v] = input("Enter neighbours: ").split()

start = input("Enter start: ")
bfs(graph, start)