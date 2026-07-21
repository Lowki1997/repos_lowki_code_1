import numpy as np

#change based on the number of rows and columns in the game
ROWS = 6
COLS = 7
PLAYER_1 = 1
PLAYER_2 = 2
EMPTY = 0

def create_board():
    """Creates an empty 6x7 grid."""
    return np.zeros((ROWS, COLS), dtype=int)

def print_board(board):
    """Prints the board upside down so row 0 is at the bottom."""
    print("\n  1   2   3   4   5   6   7")
    print("+---+---+---+---+---+---+---+")
    flipped_board = np.flipud(board)
    for row in flipped_board:
        row_str = " | ".join(
            "X" if cell == PLAYER_1 else "O" if cell == PLAYER_2 else " " 
            for cell in row
        )
        print(f"| {row_str} |")
    print("+---+---+---+---+---+---+---+")

def is_valid_location(board, col):
    """Checks if the top row of a column is empty."""
    return board[ROWS - 1][col] == EMPTY

def get_next_open_row(board, col):
    """Finds the lowest empty row in a column."""
    for r in range(ROWS):
        if board[r][col] == EMPTY:
            return r

def drop_piece(board, row, col, piece):
    """Places a piece on the board."""
    board[row][col] = piece

def check_win(board, piece):
    """Checks the board for 4-in-a-row horizontally, vertically, or diagonally."""
    for c in range(COLS - 3):
        for r in range(ROWS):
            if all(board[r][c+i] == piece for i in range(4)):
                return True

    # Check vertical locations
    for c in range(COLS):
        for r in range(ROWS - 3):
            if all(board[r+i][c] == piece for i in range(4)):
                return True

    # Check positively sloped diagonals
    for c in range(COLS - 3):
        for r in range(ROWS - 3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True

    # Check negatively sloped diagonals
    for c in range(COLS - 3):
        for r in range(3, ROWS):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True
    
    return False

def is_board_full(board):
    """Checks if there are no empty slots left."""
    return np.all(board != EMPTY)

def play_game():
    """Main game loop handles turns and inputs."""
    board = create_board()
    game_over = False
    turn = 0 

    print("Welcome to Connect Four!")
    print("Player 1 = X | Player 2 = O")
    print_board(board)

    while not game_over:
        current_player = PLAYER_1 if turn == 0 else PLAYER_2
        player_label = "Player 1 (X)" if turn == 0 else "Player 2 (O)"

        try:
            col = int(input(f"{player_label}, choose a column (1-7): ")) - 1
            if col < 0 or col > 6:
                print("Invalid column. Please choose between 1 and 7.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, current_player)
            print_board(board)

            if check_win(board, current_player):
                print(f"Congratulations! {player_label} wins!")
                game_over = True
            
  
            elif is_board_full(board):
                print("It's a tie! The board is full.")
                game_over = True

            turn = (turn + 1) % 2
        else:
            print("Column is full! Try a different one.")

if __name__ == "__main__":
    play_game()
