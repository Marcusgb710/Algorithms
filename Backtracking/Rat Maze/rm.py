def can_move(x: int, y: int, maze: list[list[int]]):
    if x >= 0 and y >=0 and x < len(maze) and y < len(maze) and maze[x][y] == 1:
        return True
    return False

def print_maze(maze: list[list[int]]):

    maze_string=""

    for i in range(len(maze)):
        maze_string += "\n" 
        for j in range(len(maze)):
            maze_string += str(maze[i][j]) + " "
    
    print(maze_string)

def rat_maze_util(x, y, maze:list[list[int]], solution: list[list[int]]):
    
    if x == len(maze)-1 and y == len(maze)-1 and maze[-1][-1] == 1:
        solution[x][y] = 1
        return True
    
    if can_move(x, y, maze):

        if solution[x][y] == 1:
            return False
        
        solution[x][y] = 1

        if rat_maze_util(x+1, y, maze, solution) == True:
            return True
        
        if rat_maze_util(x, y+1, maze, solution) == True:
            return True

        solution[x][y] = 0
        return False

    return False

def rat_maze():
    board = [[1, 0, 0, 0],
             [1, 1, 0, 1],
             [0, 1, 0, 0],
             [1, 1, 1, 1]]

    sol = [[0 for _ in range(len(board))] for _ in range(len(board))]
    if rat_maze_util(0, 0, board, sol) == False:
        print("No Solution Found")
    else:
        print("Maze: ", end="")
        print_maze(board)
        print("+--+--+")
        print("Solution: ", end="")
        print_maze(sol)

rat_maze()
