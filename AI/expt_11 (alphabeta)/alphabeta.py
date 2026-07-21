import math

def alphabeta(node, alpha, beta, tree, evals, depth=0):
    indent = "  " * depth
    children = tree.get(node, [])

    if not children:
        print(f"{indent}Terminal {node} = {evals[node]}")
        return evals[node]

    is_max = depth % 2 == 0

    if is_max:
        print(f"{indent}MAX node {node} (a={_f(alpha)}, b={_f(beta)})")
        for child in children:
            alpha = max(alpha, alphabeta(child, alpha, beta, tree, evals, depth+1))
            print(f"{indent}  a updated to {_f(alpha)}")
            if alpha >= beta:
                print(f"{indent}  >> b-pruning")
                return beta
        return alpha

    print(f"{indent}MIN node {node} (a={_f(alpha)}, b={_f(beta)})")
    for child in children:
        beta = min(beta, alphabeta(child, alpha, beta, tree, evals, depth+1))
        print(f"{indent}  b updated to {_f(beta)}")
        if alpha >= beta:
            print(f"{indent}  >> a-pruning")
            return alpha
    return beta

def _f(v):
    if v == math.inf: return "+inf"
    if v == -math.inf: return "-inf"
    return str(v)

print("Alpha-Beta Pruning")
print("==================\n")

tree, evals = {}, {}
root = None

while True:
    line = input("Node (or done): ").strip()
    if line.lower() == "done" or line == "":
        break
    parts = line.split()
    node = parts[0]
    if root is None: root = node
    if len(parts) > 1:
        tree[node] = parts[1].split(",")
    else:
        tree[node] = []
        evals[node] = int(input(f"  Value of leaf {node}: "))

print()
result = alphabeta(root, -math.inf, math.inf, tree, evals)
print(f"\nResult: {result}")