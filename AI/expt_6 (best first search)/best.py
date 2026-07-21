import heapq

n = int(input("Enter number of nodes: "))
graph = {}

for i in range(n):
    node = input(f"Enter node {i+1} name: ")
    graph[node] = input(f"Enter neighbors of {node} (space-separated): ").split()

heuristic = {}
for node in graph:
    heuristic[node] = float(input(f"Enter heuristic h({node}): "))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

def best_first_search(graph, heuristic, start, goal):
    visited = set()
    pq = [(heuristic[start], [start])]
    iteration = 1

    while pq:
        h, path = heapq.heappop(pq)
        current = path[-1]
        if current in visited: continue
        visited.add(current)
        print(f"Iteration {iteration}: Visiting {current}, h({current}) = {heuristic[current]}")
        iteration += 1
        if current == goal: return print("Goal reached!") or path
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], path + [neighbor]))
    return None

result = best_first_search(graph, heuristic, start, goal)
print("\nFinal Path from", start, "to", goal, ":", " -> ".join(result) if result
      else "\nNo path found from " + start + " to " + goal)