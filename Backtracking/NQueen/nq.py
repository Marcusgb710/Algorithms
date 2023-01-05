def can_place(row, col, board):
    
    for i in range(col):
        if board[row][i] == 1:
            return False
    # diagonal down
    
        
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False 

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False



    return True

def nqutils(board, col):

    if col >= len(board):
        return True

    for i in range(len(board)):
        if can_place(i, col, board):
            board[i][col] = 1

            if nqutils(board, col+1):
                return True
            
            board[i][col] = 0

    return False

def print_board(board):
    board_string = ""

    for i in range(len(board)):
        for j in range(len(board)):
            board_string += str(board[i][j])+ " "    
        board_string += "\n"

    print(board_string)

def nq(board_size):
    board = [[0 for _ in range(board_size)] for _ in range(board_size)]
    

    if nqutils(board, 0) == False:
        print("No Solution Found")
    else:
        print_board(board)

nq(12)



