'''
Title: poker.py
Author: Gabriel dos Reis
Date: 04/01/2024
Description: A program that simulates a poker game.

I want to check the probability of each hand.
'''
import random

def initialize_deck():
    '''Initializes a deck of cards using a tuple of tuples.'''
    deck = [("Ace", "Hearts"), ("2", "Hearts"), ("3", "Hearts"), ("4", "Hearts"), ("5", "Hearts"), ("6", "Hearts"), ("7", "Hearts"), ("8", "Hearts"), 
            ("9", "Hearts"), ("10", "Hearts"), ("Jack", "Hearts"), ("Queen", "Hearts"), ("King", "Hearts"), ("Ace", "Diamonds"), ("2", "Diamonds"), 
            ("3", "Diamonds"), ("4", "Diamonds"), ("5", "Diamonds"), ("6", "Diamonds"), ("7", "Diamonds"), ("8", "Diamonds"), ("9", "Diamonds"), 
            ("10", "Diamonds"), ("Jack", "Diamonds"), ("Queen", "Diamonds"), ("King", "Diamonds"), ("Ace", "Clubs"), ("2", "Clubs"), ("3", "Clubs"), 
            ("4", "Clubs"), ("5", "Clubs"), ("6", "Clubs"), ("7", "Clubs"), ("8", "Clubs"), ("9", "Clubs"), ("10", "Clubs"), ("Jack", "Clubs"), 
            ("Queen", "Clubs"), ("King", "Clubs"), ("Ace", "Spades"), ("2", "Spades"), ("3", "Spades"), ("4", "Spades"), ("5", "Spades"), ("6", "Spades"), 
            ("7", "Spades"), ("8", "Spades"), ("9", "Spades"), ("10", "Spades"), ("Jack", "Spades"), ("Queen", "Spades"), ("King", "Spades")]
    random.shuffle(deck)

    return deck

def display_deck(deck):
    '''Display the deck in four columns.'''
    num_columns = 4
    cards_per_column = len(deck) // num_columns

    for i in range(cards_per_column):
        for j in range(num_columns):
            index = i + j * cards_per_column
            card = deck[index]
            print(f"{card[0]:>5} of {card[1]}, ", end="\t")
        print()


def deal_cards(deck):
    ''' Deal 5 cards to the player'''
    player_hand = []
    for i in range(5):
        player_hand.append(deck.pop())
    return player_hand

def display_hand(hand):
    '''Display the hand of the player.'''
    for card in hand:
        print(f"\t{card[0]} of {card[1]}")

def is_pair(hand):
    '''Return True if the hand has a pair, False otherwise.
    A pair is two cards of the same value.
    '''
    values = [card[0] for card in hand]
    for value in values:
        if values.count(value) == 2:
            return True
    return False

def is_two_pair(hand):
    '''Return True if the hand has two pairs, False otherwise.
    Two pairs are two cards of the same value and another two cards of the same value.
    '''
    ranks = [card[0] for card in hand]
    unique_ranks = set(ranks)
    pairs = 0
    for rank in unique_ranks:
        if ranks.count(rank) == 2:
            pairs += 1
    return pairs == 2

def is_three_of_a_kind(hand):
    '''Return True if the hand has three of a kind, False otherwise.
    Three of a kind is three cards of the same value.
    '''
    values = [card[0] for card in hand]
    for value in values:
        if values.count(value) == 3:
            return True
    return False

def is_straight(hand):
    '''Return True if the hand has a straight, False otherwise.
    A straight is five cards in sequence.
    '''
    values = [card[0] for card in hand]
    values.sort()
    if values == ["10", "Jack", "Queen", "King", "Ace"]:
        return True
    for i in range(1, len(values)):
        if values[i] != values[i-1]:
            return False
    return True

def is_flush(hand):
    '''Return True if the hand has a flush, False otherwise.
    A flush is five cards of the same suit.
    '''
    suits = [card[1] for card in hand]
    return len(set(suits)) == 1

def is_full_house(hand):
    '''Return True if the hand has a full house, False otherwise.
    A full house is three of a kind and a pair.
    '''
    return is_three_of_a_kind(hand) and is_pair(hand)

def is_four_of_a_kind(hand):
    '''Return True if the hand has four of a kind, False otherwise.
    Four of a kind is four cards of the same value.
    '''
    values = [card[0] for card in hand]
    for value in values:
        if values.count(value) == 4:
            return True
    return False

def is_straight_flush(hand):
    '''Return True if the hand has a straight flush, False otherwise.
    A straight flush is a straight and a flush.'''
    return is_straight(hand) and is_flush(hand)

def is_royal_flush(hand):
    '''Return True if the hand has a royal flush, False otherwise.
    A royal flush is a straight flush with the values "10", "Jack", "Queen", "King", "Ace".'''
    values = [card[0] for card in hand]
    return is_straight_flush(hand) and values == ["10", "Jack", "Queen", "King", "Ace"]

def main():

    '''Main function.'''
    deck = initialize_deck()
    print("The deck is:", len(deck), "cards long.")
    display_deck(deck)
    hand = deal_cards(deck)
    print("\nYour hand is:")
    display_hand(hand)
    if is_royal_flush(hand):
        print("You have a Royal Flush!")
    elif is_straight_flush(hand):
        print("You have a Straight Flush!")
    elif is_four_of_a_kind(hand):
        print("You have Four of a Kind!")
    elif is_full_house(hand):
        print("You have a Full House!")
    elif is_flush(hand):
        print("You have a Flush!")
    elif is_straight(hand):
        print("You have a Straight!")
    elif is_three_of_a_kind(hand):
        print("You have Three of a Kind!")
    elif is_two_pair(hand):
        print("You have Two Pair!")
    elif is_pair(hand):
        print("You have a Pair!")
    else:
        print("You have a High Card!")


def test_hands():
    #High card
    hand0 = [("2", "Hearts"), ("3", "Diamonds"), ("4", "Clubs"), ("5", "Spades"), ("Ace", "Hearts")] # Pass - High card
    # Pair
    hand1 = [("Ace", "Hearts"), ("Ace", "Diamonds"), ("3", "Clubs"), ("7", "Spades"), ("10", "Hearts")] # Fail - You have two pairs
    # Two pair
    hand2 = [("Ace", "Hearts"), ("Ace", "Diamonds"), ("3", "Clubs"), ("3", "Spades"), ("10", "Hearts")] # Pass - you have two pair
    # Three of a kind
    hand3 = [("Ace", "Hearts"), ("Ace", "Diamonds"), ("Ace", "Clubs"), ("7", "Spades"), ("10", "Hearts")] # Pass - 3 of a kinda
    # Straight
    hand4 = [("2", "Hearts"), ("3", "Diamonds"), ("4", "Clubs"), ("5", "Spades"), ("6", "Hearts")]  # Fail - High card, should be a straight
    # Flush
    hand5 = [("2", "Hearts"), ("5", "Hearts"), ("8", "Hearts"), ("10", "Hearts"), ("King", "Hearts")] # Pass - Flush
    # Full house
    hand6 = [("Ace", "Hearts"), ("Ace", "Diamonds"), ("Ace", "Clubs"), ("10", "Spades"), ("10", "Hearts")] # Pass - Full house
    # Four of a kind
    hand7 = [("Ace", "Hearts"), ("Ace", "Diamonds"), ("Ace", "Clubs"), ("Ace", "Spades"), ("10", "Hearts")] # Pass - Four of a kind
    # Straight flush
    hand8 = [("2", "Hearts"), ("3", "Hearts"), ("4", "Hearts"), ("5", "Hearts"), ("6", "Hearts")] # Fail - Flush
    # Royal Flush
    hand9 = [("10", "Hearts"), ("Jack", "Hearts"), ("Queen", "Hearts"), ("King", "Hearts"), ("Ace", "Hearts")] # Fail - Flush

    if is_royal_flush(hand9):
        print("You have a Royal Flush!")
    elif is_straight_flush(hand9):
        print("You have a Straight Flush!")
    elif is_four_of_a_kind(hand9):
        print("You have Four of a Kind!")
    elif is_full_house(hand9):
        print("You have a Full House!")
    elif is_flush(hand9):
        print("You have a Flush!")
    elif is_straight(hand9):
        print("You have a Straight!")
    elif is_three_of_a_kind(hand9):
        print("You have Three of a Kind!")
    elif is_two_pair(hand9):
        print("You have Two Pairs!")
    elif is_pair(hand9):
        print("You have a Pair!")
    else:
        print("You have a High Card!")


if __name__ == "__main__":
    main()