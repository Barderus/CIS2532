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
    return board

def place_marker(coord_x, coord_y, player):
    '''
    This function places a marker on the board
        X or O  
    '''
    board = create_board()
    board[coord_x][coord_y] = player

def print_board():
    pass

def check_winner():
    pass

def check_draw():
    pass

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
    full = False
    
    while board is not full:
        # Player 1
        coord_x = int(input("Player 1, enter the x coordinate: "))
        coord_y = int(input("Player 1, Enter the y coordinate: "))
        place_marker(coord_x, coord_y, player1)
        print_board()
        if check_winner():
            print("We have a winner!")
            break
        if check_draw():
            print("It's a draw!")
            break
        
        # Player 2
        coord_x2 = int(input("Player 2, enter the x coordinate: "))
        coord_y2 = int(input("Player 2, Enter the y coordinate: "))
        place_marker(coord_x2, coord_y2, player2)
        print_board()
        if check_winner():
            print("We have a winner!")
            break
        if check_draw():
            print("It's a draw!")
            break

def replay():
    pass

main()