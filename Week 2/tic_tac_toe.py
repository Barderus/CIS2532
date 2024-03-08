'''
Name: Gabriel dos Reis
Date: 2021-04-07
Title: Tic-Tac-Toe game
Description: This is a Tic-Tac-Toe game that can be played by two players. It uses a 3x3 2D array to store the game board.
'''
import numpy as np
def main():
    print("\tWelcome to Tic-Tac-Toe!")
    play = input("Do you want to play? (yes/no): ")
    if play.lower() == "yes":
        play_game()
    else:
        print("\tGoodbye!")

def create_board():
    board = np.arange(1, 10).reshape(3, 3)
    board = board.astype(str)
    return board

def place_marker(board, coord_x, coord_y, player):
    '''
    This function places a marker on the board
        X or O  
    '''
    board[coord_x, coord_y] = player
    return board

# A function to print the 3x3 2D list and make it look like a board
def print_board(board):
    for item in board:
        print(item)

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

    if np.any(np.all(board == player_arr, axis=1)):
        return True

    # Columns
    if np.any(np.all(board == player_arr, axis=0)):
        return True

    # Diagonals
    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True

    return False

def check_draw(board):
    for i in range(1,10):
        if np.any(board == str(i)):
            return False
    return True

def play_game():
    '''
    This function will start the game and call all the other functions
    
    '''

    player1 = input("Player 1, do you want to be X or O? ").upper()
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"
    print(f"Player 1 is {player1} and Player 2 is {player2}")

    board = create_board()
    print(board)

    while True:
        # Player 1
        coord_x = int(input("Player 1, enter the x coordinate: ")) - 1
        coord_y = int(input("Player 1, Enter the y coordinate: ")) - 1
        board = place_marker(board, coord_x, coord_y, player1)
        print(board)

        if check_winner(board, player1):
            print("We have a winner!")
            replay()

        if check_draw(board): 
            print("It's a draw!")
            replay()
                    
        # Player 2
        coord_x2 = int(input("Player 2, enter the x coordinate: ")) - 1
        coord_y2 = int(input("Player 2, Enter the y coordinate: ")) - 1
        board = place_marker(board, coord_x2, coord_y2, player2)
        print(board)
        if check_winner(board, player2):
            print("We have a winner!")
            replay()

        if check_draw(board):
            print("It's a draw!")
            replay()

def replay():
    
    replay = input("Would you like to play again? (y/n): ").lower()
    if replay == "y":
        play_game()
    else:
        print("It was nice playing with you. See you next time.")

main()