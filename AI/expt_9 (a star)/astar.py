import heapq

def a_star(graph, heuristics, start, goal_set):
    queue = [(heuristics[start], 0, start, [start])]
    visited = set()
    iteration = 1

    while queue:
        est_total, cost, node, path = heapq.heappop(queue)
        if node in visited: continue

        print(f"Iteration {iteration}: Visiting {node}")
        print(f"  g({node}) = {cost}")
        print(f"  h({node}) = {heuristics[node]}")
        print(f"  f({node}) = {est_total}")
        print(f"  Path so far: {' -> '.join(path)}\n")
        iteration += 1

        if node in goal_set:
            print("Goal reached!")
            print("Final Path:", " -> ".join(path))
            print("Total Cost:", cost)
            return

        visited.add(node)
        for neighbor, edge_cost in graph.get(node, []):
            if neighbor not in visited:
                new_cost = cost + edge_cost
                heapq.heappush(queue, (new_cost + heuristics[neighbor], new_cost, neighbor, path + [neighbor]))
    print("No path found.")

graph, heuristics = {}, {}
n = int(input("Enter number of nodes: "))
for _ in range(n):
    name = input("Enter node name: ")
    heuristics[name] = int(input(f"Heuristic of {name}: "))
    graph[name] = []

e = int(input("Enter number of edges: "))
for _ in range(e):
    u, v, c = input("Enter edge (from to cost): ").split()
    graph[u].append((v, int(c)))

start = input("Enter start node: ")
goal_set = set(input("Enter goal nodes (space-separated): ").split())
a_star(graph, heuristics, start, goal_set)