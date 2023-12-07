#Author: Christine Yang-Dai
#Student no: 260990057

from card2 import *

def draw(hand, top_discard_card):
    '''
    (list, int) -> str
    
    Takes a list of the cards in the player’s hand as argument, as well as the card currently at
    the top of the discard pile. Asks the user to enter either 'stock' or 'discard' and returns
    that string.
    
    >>> draw([12, 34, 2], 3)
    Draw location: stock
    'stock'
    
    >>> draw([12, 34, 2], 3)
    Draw location: restock
    Invalid option.
    Draw location: discard
    'discard'
    
    >>> draw([12, 34, 2], None)
    Draw location: discard
    'discard'
    '''
    action_range = ["stock", "discard"]
    action = input("Draw location: ")
    while action not in action_range:
        print("Invalid option.")
        action = input("Draw location: ")
    return action

def discard(hand):
    '''
    (list) -> int
    
    Takes a list of the cards in the player’s hand as argument. Prints out each card and its index
    in the list. Asks the user to enter one of the indices, and returns the card at that index.
    
    >>> discard([1, 2, 53, 12])
    0    TWO of HEARTS
    1    TWO of DIAMONDS
    2    TWO of HEARTS
    3    FOUR of SPADES
    Choice: 3
    12
    
    >>> discard([1, 2, 53, 12, 34, 51])
    0    TWO of HEARTS
    1    TWO of DIAMONDS
    2    TWO of HEARTS
    3    FOUR of SPADES
    4    TEN of DIAMONDS
    5    ACE of CLUBS
    Choice: 4
    34
    
    >>> discard([51, 7, 23])
    0    ACE of CLUBS
    1    THREE of CLUBS
    2    SEVEN of CLUBS
    Choice: 3
    Invalid card.
    Choice: 0
    51
    '''
    for h in range(len(hand)):
        print(h, '\t', card_to_string(hand[h]))
        
    choice = int(input("Choice: "))
    
    while 0 > choice or choice > (len(hand) - 1):
        print("Invalid card.")
        choice = int(input("Choice: "))
    
    return hand[choice]