board = [['_' for j in range(3)] for i in range(3)]

def print_board():
    for row in board:
        print(*row)

def check_win(player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def minimax(is_maximizing):
    if check_win('O'):
        return 10
    if check_win('X'):
        return -10
    if all(cell != '_' for row in board for cell in row):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == '_':
                    board[row][col] = 'O'
                    best_score = max(best_score, minimax(False))
                    board[row][col] = '_'
        return best_score

    best_score = float('inf')
    for row in range(3):
        for col in range(3):
            if board[row][col] == '_':
                board[row][col] = 'X'
                best_score = min(best_score, minimax(True))
                board[row][col] = '_'
    return best_score

def best_move():
    best_score = float('-inf')
    move = None

    for row in range(3):
        for col in range(3):
            if board[row][col] == '_':
                board[row][col] = 'O'
                score = minimax(False)
                board[row][col] = '_'
                if score > best_score:
                    best_score, move = score, (row, col)
    return move

def tic_tac_toe():
    print_board()

    try:
        while True:
            print("\nYour turn")
            try:
                row, col = map(int, input("Enter row and column (0-2): ").split())
            except:
                print("Invalid input. Enter like: 0 0")
                continue

            if row not in range(3) or col not in range(3):
                print("Out of bounds. Try again.")
                continue

            if board[row][col] != '_':
                print("Invalid move. Try again.")
                continue

            board[row][col] = 'X'
            print_board()

            if check_win('X'):
                print("Player X wins!")
                break

            if all(cell != '_' for row in board for cell in row):
                print("It's a tie!")
                break

            print("\nComputer's turn")
            move = best_move()
            if move:
                board[move[0]][move[1]] = 'O'
                print_board()

                if check_win('O'):
                    print("Computer wins!")
                    break
    except KeyboardInterrupt:
        print("\nGame terminated.")

tic_tac_toe()