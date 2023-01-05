

GRID_SIZE = 8



def is_safe(x: int, y: int, board: list[list[int]]):
    if x >= 0 and x < GRID_SIZE and y >= 0 and y < GRID_SIZE and board[x][y] == -1:
        return True
    return False

def print_board(board):
    board_string = ""

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            board_string += str(board[i][j])+ " "    
        board_string += "\n"
    
    print(board_string)

def kt_util(x:int, y: int, move_integer: int, board: list[list[int]], x_moves: list[int], y_moves: list[int]):
    # print(move_integer)
    if move_integer == GRID_SIZE * GRID_SIZE:
        return True

    for i in range(GRID_SIZE):
        NEXT_X_MOVE: int = x + x_moves[i]
        NEXT_Y_MOVE: int = y + y_moves[i]
        # print(is_safe(NEXT_X_MOVE, NEXT_Y_MOVE, board))

        if is_safe(NEXT_X_MOVE, NEXT_Y_MOVE, board):
            board[NEXT_X_MOVE][NEXT_Y_MOVE] = move_integer
            # print(board)

            if (kt_util(NEXT_X_MOVE, NEXT_Y_MOVE, move_integer + 1, board, x_moves, y_moves)):
                # print(board, f"\n X:{NEXT_X_MOVE}, Y:{NEXT_Y_MOVE}, MI:{move_integer}")
                return True
            
            
            board[NEXT_X_MOVE][NEXT_Y_MOVE] = -1
            # print(board, f"\n X:{NEXT_X_MOVE}, Y:{NEXT_Y_MOVE}, MI:{move_integer}")

    return False



def solve_kt():
    board = [[-1 for _ in range(GRID_SIZE)]for _ in range(GRID_SIZE)]
    print(board)
    x_move = [2, 1, -1, -2, -2, -1, 1, 2]
    y_move = [1, 2, 2, 1, -1, -2, -2, -1]

    board[0][0] = 0
    # kt_util(0, 0, 1, board, x_move, y_move)
    pos = 1

    if not kt_util(0, 0, pos, board, x_move, y_move):
        print("No solution")
    else:
        print_board(board)
    
solve_kt()





