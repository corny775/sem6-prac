def steepest_hill_climbing(graph, start, heuristic_values):
    current = start
    path = [current]

    while True:
        neighbors = graph.get(current, [])
        next_node = None
        best_h = heuristic_values[current]

        for neighbor in neighbors:
            if heuristic_values[neighbor] < best_h:
                best_h = heuristic_values[neighbor]
                next_node = neighbor

        if next_node is None:
            break

        current = next_node
        path.append(current)

    return path

graph = {}
heuristic_values = {}

while True:
    node = input("Enter node (or 'done' to finish): ").strip()
    if node.lower() == "done":
        break
    graph[node] = input(f"Enter neighbors for {node}: ").split()

print("\nEnter heuristic values:")
for node in graph:
    heuristic_values[node] = int(input(f"Heuristic value for {node}: "))

start_node = input("\nEnter start node: ").strip()
final_path = steepest_hill_climbing(graph, start_node, heuristic_values)

print("Path:", " -> ".join(final_path))