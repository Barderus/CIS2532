'''
Name: Gabriel dos Reis
Date: 3/13/2024
Title: Tic-Tac-Toe game
Description: This is a Tic-Tac-Toe game that can be played by a player vs computer. It uses a 3x3 2D array to store the game board.
'''
import numpy as np
import random as rand

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

def is_marked(board, coord_x, coord_y):
    """
    Checks if a space on the Tic-Tac-Toe board is marked.

    Parameters:
    - board (numpy.ndarray): A 3x3 numpy array representing the Tic-Tac-Toe board.
    - coord_x (int): The x-coordinate (row index) of the space to check.
    - coord_y (int): The y-coordinate (column index) of the space to check.

    Returns:
    - True if the space is marked, False otherwise.
    """

    if board[coord_x, coord_y] == "X" or board[coord_x, coord_y] == "O":
        return True
    return False

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

    # Prompt players to choose their markers
    while True:
        player1 = input("Player 1, do you want to be X or O? ").upper()
        if player1 == "X":
            pc = "O"
            break
        elif player1 == "O":
            pc = "X"
            break
        else:
            print("Invalid input. Please choose 'X' or 'O'.")

    print(f"Player 1 is {player1} and PC is {pc}")

    # Create an empty game board
    board = create_board()
    print()
    print_board(board)

    # Main game loop
    while True:
        # Player 1's turn
        while True:
            try:
                # Get coordinates for Player 1's move
                coord_x = int(input("\nPlayer 1, enter the x coordinate: ")) - 1
                coord_y = int(input("Player 1, Enter the y coordinate: ")) - 1

                # Check if coordinates are within bounds
                if coord_x < 0 or coord_y < 0 or coord_x > 2 or coord_y > 2:
                    print("Invalid coordinates. Please enter numbers between 1 and 3.")
                    continue
            except ValueError:
                print("Invalid input. Please enter integers.")
                continue
            
            # Check if the selected position is already marked
            if is_marked(board, coord_x, coord_y):
                print("This position is already occupied. Please choose another position.")
            else:
                # Place Player 1's marker on the board
                board = place_marker(board, coord_x, coord_y, player1)
                break  # Exit the loop when a valid position is entered

        print()
        print_board(board)

        # Check if Player 1 wins or the game ends in a draw
        if check_winner(board, player1):
            print("\n\tWe have a winner! Player 1 wins!")
            replay()

        if check_draw(board): 
            print("\n\tIt's a draw!")
            replay()
                    
        # PC's turn
        while True:
            # Get coordinates for PC move
            x_coord_rand = rand.randint(0,2)
            y_coord_rand = rand.randint(0,2)
            
            # Check if the selected position is already marked
            if is_marked(board, x_coord_rand, y_coord_rand):
                print()
            else:
                # Place PC's marker on the board
                board = place_marker(board, x_coord_rand, y_coord_rand, pc)
                break  # Exit the loop when a valid position is entered
        
        print()
        print_board(board)

        # Check if PC wins or the game ends in a draw
        if check_winner(board, pc):
            print("\n\tWe have a winner! PC!")
            replay()

        if check_draw(board):
            print("\n\tIt's a draw!")
            replay()

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
