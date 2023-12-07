#Author: Christine Yang-Dai
#This program can find the suit and the rank of the cards (numbered from 1 to 52) of a playing deck.
#It can also compare the color, rank and suit 2 cards.

#variables, the value that corresponds to each rank/suit
HEARTS = 0
DIAMONDS = 1
CLUBS = 2
SPADES = 3

TWO = 0
THREE = 1
FOUR = 2
FIVE = 3
SIX = 4
SEVEN = 5
EIGHT = 6
NINE = 7
TEN = 8
JACK = 9
QUEEN = 10
KING = 11
ACE = 12

def get_suit(card):
    '''
    (int) -> int
    
    Take in an integer representing the card. Return an integer between 0
    and 3 representing the suit.
    
    >>> get_suit(1)
    0
    
    >>> get_suit(3)
    2
    
    >>> get_suit(52)
    3
    
    >>> get_suit(18)
    1
    '''
    if card % 4 == 0:
        return 3
    elif card % 4 == 3:
        return 2
    elif card % 4 == 2:
        return 1
    else:
        return 0

def get_rank(card):
    '''
    (int) -> int
    
    Take in an integer representing the card. Return an integer between 0
    and 12 representing the rank.
    
    >>> get_rank(1)
    0
    
    >>> get_rank(52)
    12
    
    >>> get_rank(6)
    1
    '''
    return (card - 1) // 4

def same_rank(card1, card2):
    '''
    (int, int) -> bool
    
    Compare the rank of 2 cards, given with integers are the same.
    Return true if they are the same, false otherwise.
    
    >>> same_rank(52, 6)
    False
    
    >>> same_rank(1, 2)
    True
    
    >>> same_rank(6, 9)
    False
    
    >>> same_rank(9, 10)
    True
    '''
    return(bool (get_rank(card1) == get_rank(card2)))

def same_suit(card1, card2):
    '''
    (int, int) -> bool
    
    Compare the suit of 2 cards, given with integers are the same.
    Return true if they are the same, false otherwise.
    
    >>> same_suit(52, 16)
    True
    
    >>> same_suit(19, 1)
    False
    
    >>> same_suit(19, 3)
    True
    '''
    return(bool(get_suit(card1) == get_suit(card2)))

def same_color_suit(card1, card2):
    '''
    (int, int) -> bool
    
    Compare the color of 2 cards, given with integers are the same.
    Return true if they are the same, false otherwise.
    
    >>> same_color_suit(1, 5)
    True
    
    >>> same_color_suit(52, 4)
    True
    
    >>> same_color_suit(1, 4)
    False
    '''
    if get_suit(card1) < 2:
        color1 = 'red'
    else:
        color1 = 'black'
    
    if get_suit(card2) < 2:
        color2 = 'red'
    else:
        color2 = 'black'
    
    return(bool (color1 == color2))
    