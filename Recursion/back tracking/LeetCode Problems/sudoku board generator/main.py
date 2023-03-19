def valid_sudoku_row_and_column(board):
    for horizontal in range(0, len(board)):
        for vertical in range(0, len(board)):
            if not (vertical + 1 in board[horizontal]):
                return False
            if not (horizontal + 1 in board[vertical]):
                return False
    return True

def valid_sudoku_grid(board):
    arrayStart = 0
    arrayEnd = 2
    arrayIndexStart = 0
    arrayIndexEnd = 2
  
    while(True):
        validateThis = [];

        for start in range(arrayStart, arrayEnd+1):
            for startFrom in range(arrayIndexStart, arrayIndexEnd+1):
                validateThis.append(board[start][startFrom])

        for sudokuValue in range(1, len(board)+1):
            if not (sudokuValue in validateThis):
                return False
    
        arrayIndexStart += 3;
        arrayIndexEnd += 3;

        if arrayIndexStart == 9 and arrayIndexEnd == 11:
            arrayStart += 3
            arrayEnd += 3
            arrayIndexStart = 0
            arrayIndexEnd = 2

        if arrayStart == 9 and arrayEnd == 11:
            return True
      
def valid_sudoku_board(board):
    valid_rows_cols = valid_sudoku_row_and_column(board)

    if(not valid_rows_cols): return False
    
    valid_grids = valid_sudoku_grid(board)
    
    if(not valid_grids): return False

    return True

def generate_board():
    board = [[None]*9 for i in range(9)]
    return valid_sudoku_board(board)

print(generate_board())

print(valid_sudoku_board([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
])) # true

print(valid_sudoku_board([
  [5, 3, 4, 6, 7, 8, 9, 1, 2], 
  [6, 7, 2, 1, 9, 0, 3, 4, 8],
  [1, 0, 0, 3, 4, 2, 5, 6, 0],
  [8, 5, 9, 7, 6, 1, 0, 2, 0],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 0, 1, 5, 3, 7, 2, 1, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 0, 0, 4, 8, 1, 1, 7, 9]
])) # false