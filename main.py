# Function to print the game board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check for a win or tie
def check_win(board):
    # All possible winning combinations
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                        (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                        (0, 4, 8), (2, 4, 6)]
    
    # Check if any combination has the same player mark
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return board[combo[0]]  # Return the winner ('X' or 'O')
    
    # Check for tie (if the board is full and no winner)
    if ' ' not in board:
        return 'Tie'
    
    return None  # Game is still going

# Main game loop
def tic_tac_toe():
    board = [' '] * 9  # Empty board
    current_player = 'X'  # 'X' starts first
    
    while True:
        print_board(board)
        
        try:
            move = int(input(f"Player {current_player}, choose your move (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != ' ':
                print("Invalid move! Try again.")
                continue
            board[move] = current_player
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")
            continue
        
        # Check for winner or tie
        result = check_win(board)
        if result == 'X':
            print_board(board)
            print("Player X wins!")
            break
        elif result == 'O':
            print_board(board)
            print("Player O wins!")
            break
        elif result == 'Tie':
            print_board(board)
            print("It's a tie!")
            break
        
        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
