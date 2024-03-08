'''
Name: Gabriel dos Reis
Date: 2021-04-07
Title: Tic-Tac-Toe game
Description: This is a Tic-Tac-Toe game that can be played by one players versus a computer. It uses a 3x3 2D array to store the game board.
'''
import numpy as np

def main():
    print("\tWelcome to Tic-Tac-Toe!")
    play = input("Do you want to play? (yes/no): ")
    if play.lower() == "yes":
        play_game()
    else:
        print("\tThank you! See you later!!")

def create_board():
    """
    Create a 3x3 board for a Tic-Tac-Toe game.

    Returns:
    - board (numpy.ndarray): A 3x3 numpy array representing the Tic-Tac-Toe board.

    The function creates a 3x3 numpy array representing the Tic-Tac-Toe board with
    numbers 1 through 9 assigned as initial placeholders for each cell. This function
    is used to initialize the game board before starting a new game.
    """
    board = np.arange(1, 10).reshape(3, 3)
    board = board.astype(str)
    return board

def place_marker(board, coord_x, coord_y, player):
    """
    Place a marker on the Tic-Tac-Toe board at specified coordinates.

    Parameters:
    - board (numpy.ndarray): A 3x3 numpy array representing the Tic-Tac-Toe board.
    - coord_x (int): The x-coordinate (row index) where the marker will be placed.
    - coord_y (int): The y-coordinate (column index) where the marker will be placed.
    - player (str): The marker to be placed on the board. It can be 'X' or 'O'.

    Returns:
    - board (numpy.ndarray): The updated Tic-Tac-Toe board after placing the marker.

    The function modifies the Tic-Tac-Toe board by placing the specified marker ('X' or 'O')
    at the given coordinates (coord_x, coord_y). 
    """

    board[coord_x, coord_y] = player
    return board

def print_board(board):
    """
    Print the Tic-Tac-Toe board.

    Parameters:
    - board (numpy.ndarray): A 3x3 numpy array representing the Tic-Tac-Toe board.

    The function prints the Tic-Tac-Toe board to the console. Each row of the board
    is printed as a separate line, with the elements separated by spaces.
    """

    for row in range(len(board)):
        # Print each row of the board
        for col in range(len(board[row])):
            # Print each column of the board
            print(" " + str(board[row][col]) + " ", end="")
            if col < len(board[row]) - 1:
                print("|", end="")
        print()  # Move to the next line

        if row < len(board) - 1:
            # Print horizontal lines between rows
            print("-" * (len(board) * 4 - 1))

def pc_move(board, pc):
    """
    First, get the computer player to make a random (valid) move. Pick a random X and random Y, 
    check if that cell is occupied. Make the move, or pick new numbers

    Second, if there is a winning move to make, make it! For every valid move: 
    make the move, see if it has won, unmake the move if not, and try the next move. 
    If there's no winning move, make a random move

    Third: restructure your code so you can copy a board, and see if there is a winning move on that board. 
    For each valid move: copy the board, make the move on the copy, check the copy of the board for a win, etc.

    Fourth: for each valid move, make the move as your opponent on a copy of the board. 
    If it's a winner, make the move as you since you're blocking the opponent from winning. 
    (Having first checked that there's no move that allows you to win). Random move otherwise.
    
    For AI use minimax algorithm
    
    """

def check_winner(board, player):
    '''
    Check if the specified player has won the game.
    
    Parameters:
    - board: A 3x3 NumPy array representing the current state of the game board.
    - player: The player's marker ('X' or 'O') to check for a win.
    
    Returns:
    - True if the specified player has won the game, False otherwise.
    '''
    # Define the array for the specified player's markers
    player_arr = np.full((3, 3), player)

    # Check rows for win
    if np.any(np.all(board == player_arr, axis=1)):
        return True

    # Check Columns for win
    if np.any(np.all(board == player_arr, axis=0)):
        return True

    # Check Diagonals for win
    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True

    return False

def check_draw(board):
    for i in range(1,10):
        if np.any(board == str(i)):
            return False
    return True

def play_game():
    """
    Start and manage the Tic-Tac-Toe game.

    This function initiates the Tic-Tac-Toe game by prompting Player 1 to choose
    either 'X' or 'O'. It then sets up the game board, displays it, and allows
    players to make moves alternately. The game continues until a player wins or
    the game ends in a draw.

    The game flow includes the following steps:
    1. Player 1 chooses 'X' or 'O', and Player 2 gets assigned the opposite marker.
    2. The initial empty game board is displayed.
    3. Players take turns entering coordinates to place their markers on the board.
    4. After each move, the board is updated and displayed.
    5. The game continues until one player wins or the game ends in a draw.
    6. Once the game concludes, players have the option to replay.

    """

    player1 = input("Player 1, do you want to be X or O? ").upper()
    if player1 == "X":
        pc = "O"
    else:
        pc = "X"
    print(f"Player 1 is {player1} and Compuer is {pc}")

    board = create_board()
    print()
    print_board(board)

    while True:
        # Player 1
        coord_x = int(input("\nPlayer 1, enter the x coordinate: ")) - 1
        coord_y = int(input("Player 1, Enter the y coordinate: ")) - 1
        board = place_marker(board, coord_x, coord_y, player1)
        print()
        print_board(board)

        if check_winner(board, player1):
            print("\nWe have a winner!")
            replay()

        if check_draw(board): 
            print("It's a draw!")
            replay()

        # PC move
        pc_move(board, pc)
                    

def replay():
    """
    Check if the user would like to play again.

    This function prompts the user to decide whether they want to play the Tic-Tac-Toe game again.
    If the user inputs 'y' for yes, the game is restarted by calling the `play_game()` function.
    If the user inputs 'n' for no, a farewell message is displayed, and the program exits.
    """
    
    replay = input("Would you like to play again? (y/n): ").lower()
    if replay == "y":
        play_game()
    else:
        print("It was nice playing with you. See you next time.")
        exit()

if __name__ == "__main__":
    main()
