# This function is called by def solver() to see if a proposed number is valid
def check_validity(board, row, col, num):
    for c in range(9):
        if board[row][c] == num:
            return False

    for r in range(9):
        if board[r][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False

    return True


# This function solves the puzzle using backtracking
def solver(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if check_validity(board, row, col, num):
                        board[row][col] = num
                        if solver(board):
                            return True
                        board[row][col] = 0
                return False
    return True
