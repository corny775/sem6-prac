def simple_hill_climbing(graph, start, heuristic_values):
    current = start
    path = [current]
    step = 1

    while True:
        neighbors = graph.get(current, [])
        next_node = None

        for neighbor in neighbors:
            if heuristic_values[neighbor] < heuristic_values[current]:
                next_node = neighbor
                break

        if next_node is None:
            break

        current = next_node
        path.append(current)
        step += 1

    return path

graph = {}
heuristic_values = {}

while True:
    node = input("Enter node (or 'done' to finish): ").strip()
    if node.lower() == 'done':
        break
    graph[node] = [n.strip() for n in input(f"Enter neighbors for {node}: ").strip() if n.strip()]

print("\nEnter heuristic values:")
for node in graph:
    heuristic_values[node] = int(input(f"Heuristic value for {node}: "))

start_node = input("\nEnter start node: ").strip()
final_path = simple_hill_climbing(graph, start_node, heuristic_values)

print(" -> ".join(final_path))