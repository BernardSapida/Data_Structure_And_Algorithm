import random

def valid_sudoku_row_and_column(board):
    x = [0]*9
    y = [0]*9

    for i in range(0, len(board)):
        for j in range(0, len(board)):
            x[i] += board[i][j]
            y[j] += board[j][i]

    return True

def valid_sudoku_grid(board):
    box = [[0,0,0] for i in range(3)]

    for i in range(9):
        for j in range(9):
            box[int(i/3)][int(j/3)] += board[i][j]

    for i in range(len(box)):
        if not (box[0][i] == box[1][i] == box[2][i]):
            return False

    return True
      
def valid_sudoku_board(board):
    valid_rows_cols = valid_sudoku_row_and_column(board)

    if(not valid_rows_cols): return False
    
    valid_grids = valid_sudoku_grid(board)
    
    if(not valid_grids): return False

    return True

def get_empty_spot_index(current_board_state):
    for i in range(9):
        for j in range(9):
            if current_board_state[i][j] == 0:
                return [i, j]
    return -1

def valid_spot(current_board_state, coordinate, number):
    x, y = coordinate
    gridX = int(x/3)
    gridY = int(y/3)

    # horizontal checking
    for i in range(0, 9):
        if current_board_state[x][i] == number:
            return False
        
    # vertical checking
    for i in range(0, 9):
        if current_board_state[i][y] == number:
            return False   
    
    # 3x3 grid checking
    for i in range(gridX*3, gridX*3+3):
        for j in range(gridY*3, gridY*3+3):
            if current_board_state[i][j] == number:
                return False
        
    return True

def display_board(board):
    for i in range(9):
        print(board[i])

def generate_board(current_board_state = [[0]*9 for i in range(9)]):
    empty_coords = get_empty_spot_index(current_board_state)

    if empty_coords == -1:
        return current_board_state

    for n in range(1, 10):
        is_valid_spot = valid_spot(current_board_state, empty_coords, n)

        if is_valid_spot:
            x, y = empty_coords

            current_board_state[x][y] = n

            if(generate_board(current_board_state)):
                return current_board_state
            
            current_board_state[x][y] = 0

    return False

def shuffle(n):
    return random.randint(0, 10) - n

# Generate 10 sudoku board
for _ in range(10):
    board = [[1, 2, 3, 4, 5, 6, 7, 8, 9] if i == 0 else [0]*9 for i in range(9)]
    board[0].sort(key = shuffle)
    generated_board = generate_board(board)

    display_board(generated_board)
    print("Valid Sudoku: " + str(valid_sudoku_board(generated_board)))
    print()

# print(valid_sudoku_board([
#   [5, 3, 4, 6, 7, 8, 9, 1, 2],
#   [6, 7, 2, 1, 9, 5, 3, 4, 8],
#   [1, 9, 8, 3, 4, 2, 5, 6, 7],
#   [8, 5, 9, 7, 6, 1, 4, 2, 3],
#   [4, 2, 6, 8, 5, 3, 7, 9, 1],
#   [7, 1, 3, 9, 2, 4, 8, 5, 6],
#   [9, 6, 1, 5, 3, 7, 2, 8, 4],
#   [2, 8, 7, 4, 1, 9, 6, 3, 5],
#   [3, 4, 5, 2, 8, 6, 1, 7, 9]
# ])) # true

# print(valid_sudoku_board([
#   [5, 3, 4, 6, 7, 8, 9, 1, 2], 
#   [6, 7, 2, 1, 9, 0, 3, 4, 8],
#   [1, 0, 0, 3, 4, 2, 5, 6, 0],
#   [8, 5, 9, 7, 6, 1, 0, 2, 0],
#   [4, 2, 6, 8, 5, 3, 7, 9, 1],
#   [7, 1, 3, 9, 2, 4, 8, 5, 6],
#   [9, 0, 1, 5, 3, 7, 2, 1, 4],
#   [2, 8, 7, 4, 1, 9, 6, 3, 5],
#   [3, 0, 0, 4, 8, 1, 1, 7, 9]
# ])) # false