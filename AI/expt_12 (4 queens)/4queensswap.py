N = 4
cols = list(range(N))

def safe_partial(k):
    for i in range(k):
        for j in range(i + 1, k + 1):
            if abs(cols[i] - cols[j]) == abs(i - j):
                return False
    return True

def solve_swap(k=0):
    if k >= N:
        return True
    for i in range(k, N):
        cols[k], cols[i] = cols[i], cols[k]
        if safe_partial(k) and solve_swap(k + 1):
            return True
        cols[k], cols[i] = cols[i], cols[k]
    return False

def print_solution():
    for r in range(N):
        print(' '.join('Q' if cols[c] == r else '.' for c in range(N)))

if solve_swap():
    print("Solution Found:\n")
    print_solution()
else:
    print("No Solution Exists")