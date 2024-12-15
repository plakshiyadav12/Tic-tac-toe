# Tic Tac Toe Game
def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """Checks if there's a winner."""
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":  # Row
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":  # Column
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_full(board):
    """Checks if the board is full."""
    return all(cell != " " for row in board for cell in row)

def main():
    """Main game loop."""
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        print(f"Player {players[current_player]}'s turn.")
        try:
            # Take input for the row and column
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            
            # Check if the cell is empty
            if board[row][col] == " ":
                board[row][col] = players[current_player]  # Place the player's mark
                print_board(board)

                # Check for a winner
                winner = check_winner(board)
                if winner:
                    print(f"Player {winner} wins!")
                    break

                # Check for a tie
                if is_full(board):
                    print("It's a tie!")
                    break

                # Switch players
                current_player = 1 - current_player
            else:
                print("Cell already occupied! Choose another.")
        except (ValueError, IndexError):
            print("Invalid input! Enter numbers between 0 and 2.")

if __name__ == "__main__":
    main()
