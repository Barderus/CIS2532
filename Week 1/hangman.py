'''
Author: Gabriel dos Reis
Date: 2/25/2024
Program: hangman.py
Description: Hangman game with a dictionary of 12 words. The user has 12 tries to guess the word. 
On the 10th try, the user can ask for a hint.
'''

import random


def main():
    print("\n\tWelcome to the Hangman Game!")
    play_game()
    name = input("\nPlease, enter your name: ")
    ready = input(f"{name}, are you ready to play? (yes/no)")
    if ready.lower() == "yes":
        play_game()
    else:
        print("See you next time!")

def play_game():

    #name = input("Please, enter your name: ")
    
    # Dictionary with the 12 words
    words_dict = {"house":"An object you see everyday", 
                  "parakeet":"a bird many people have as a pet", 
                  "cellphone":"a common object in everyone's lives",
                  "supermarket":"This word refers to a place", 
                  "lawyer":"a profession", 
                  "batman":"a comic book character", 
                  "candle":"an object found at home", 
                  "maine":"a state in the USA", 
                  "jacket":"a piece of clothing", 
                  "neptune":"an object found in space", 
                  "concrete":"a construction material", 
                  "diamond":"a gem"}
    
    # Create a list with the keys (words) of the dictionary and randomly choose a key
    keys = list(words_dict)
    #print("Words of the dictionary:", keys)
    word = random.choice(keys)
    #print("Word randomly chosen from the list of words (keys)", word)
    
    # Store the letters in the word using list comprehension
    breakdown_word = [letter for letter in word]
    #print("Word breakdown:", breakdown_word)
    
    # Store the letters already guessed
    guessed_letters = []
    
    # Hint
    hint = words_dict[word]
    #print("Hint:", hint)
    
    # Track the number of tries
    tries = 0
    max_tries = 12
        
    # Create a list of underscores to represent the secret word
    secret_word = ["_"] * len(word)
    print("Secret word:", secret_word)
    
    # Get user guess
    while tries < max_tries and "_" in secret_word:
        guess = input("Enter your guess: ").lower()
        if guess in guessed_letters:                    # Check if the user had already guessed the letter
            print("You already guessed that letter.")
        else:
            guessed_letters.append(guess)
            if guess in breakdown_word:         # Check if the user's guess is in the word
                print("\nCorrect guess!")
                # Replace the underscore with the correct letter
                for i, letter in enumerate(breakdown_word):
                    if letter != "_" and guess == letter:
                        secret_word[i] = guess
                print("Secret word:", secret_word)
            
            else:
                print("\nIncorrect guess.")
                max_tries -= 1 # Decrement the number of tries
                
                # If the user has 2 tries left, ask if they want a hint
                if max_tries == 2:
                    ask_hint = input("Would you like a hint? (yes or no): ").lower()
                    if ask_hint == "yes":
                        print(words_dict[word])
                    else:
                        print("Good luck!")
                        
                print(hangman_graphic(max_tries // 2)) # Print the hangman graphic
                print(f"You have {max_tries - tries} tries left.")
                print("Secret word:", secret_word)
            
            # If the user has no more tries left, end the game
            if max_tries == 0:
                print(f"\nSorry, you lost! The word was: {word}.")
                play_again = input("Would you like to play again? (yes or no) ")
                if play_again.lower() == "yes":
                    play_game()
                else:
                    break
    # If the user guessed the word, end the game
    if "_" not in secret_word:
        print(f"\nCongratulations! You guessed the word: {word}.")
        play_again = input("Would you like to play again? (yes or no) ")
        if play_again.lower() == "yes":
            play_game()
        else:
            print("See you next time!")    
                
                
def hangman_graphic(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

# Call the main function            
if __name__ == "__main__":  
    main()
    
    
    