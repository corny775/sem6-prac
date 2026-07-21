def print_board(board, n, solutions):
    print(f"\nSolution {len(solutions)}:")
    for i in range(n):
        for j in range(n):
            print("Q" if board[i] == j else "_", end=" ")
        print()

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def Nqueens(board, row, n, solutions):
    if row == n:
        solutions.append(board.copy())
        print_board(board, n, solutions)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            Nqueens(board, row + 1, n, solutions)
            board[row] = -1

n = 4
board = [-1] * n
solutions = []
Nqueens(board, 0, n, solutions)
print(f"\nTotal solutions found: {len(solutions)}")