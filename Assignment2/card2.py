#Author: Christine Yang-Dai
#Student no: 260990057
from card1 import *

SUITS = [0, 1, 2, 3]
RANKS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
SUITS_STR = ['HEARTS', 'DIAMONDS', 'CLUBS', 'SPADES']
RANKS_STR = ['TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING', 'ACE']

def get_card(suit, rank):
    '''
    (int, int) -> int
    
    takes two integers as arguments (one for a suit between 0 and 3, and the other
    for a rank between 0 and 12), and returns the integer representation of the
    card with that suit and rank (i.e., a number between 1 and 52).
    
    >>> get_card(0, 0)
    1
    
    >>> get_card(10, 1)
    15

    >>> get_card(3, 7)
    32
    '''
    return rank * 4 + 1 + suit

def card_to_string(card):
    '''
    (int) -> str
    
    Takes an integer as argument for a card between 1 and 52, and returns a
    string for that card’s name in the form RANK of SUIT.
    
    >>> card_to_string(17)
    'SIX of HEARTS'
    
    >>> card_to_string(38)
    'JACK of DIAMONDS'
    
    >>> card_to_string(24)
    'SEVEN of SPADES
    '''
    i = 0
    while i < len(RANKS):
        if RANKS[i] == (get_rank(card)):
            rank = RANKS_STR[i]
            i = len(RANKS)
        else:
            i += 1
    
    j = 0
    while j < len(SUITS):
        if SUITS[j] == (get_suit(card)):
            suit = SUITS_STR[j]
            j = len(SUITS)
        else:
            j += 1
    return  rank + ' of ' + suit

def hand_to_string(hand):
    '''
    (list) -> str
    
    Takes a list of cards between 1 and 52 as argument, and returns a string containing
    the names of all the cards, each card name being separated by a comma and a space.
    
    >>> hand_to_string([49, 50, 51, 52])
    'ACE of HEARTS, ACE of DIAMONDS, ACE of CLUBS, ACE of SPADES'
    
    >>> hand_to_string([9, 14, 19, 24])
    'FOUR of HEARTS, FIVE of DIAMONDS, SIX of CLUBS, SEVEN of SPADES'
    
    >>> hand_to_string([34])
    'TEN of DIAMONDS'
    '''
    hand_str = ''
    for c in range(len(hand)):
        if hand[c] == hand[-1]:
            hand_str += card_to_string(hand[c])
        else:
            hand_str += card_to_string(hand[c]) + ', '
    return hand_str

def get_deck():
    '''
    () -> list
    
    Returns a list of integers containing the 52 cards in a deck of playing cards.
    
    >>> get_deck()
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
    24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44,
    45, 46, 47, 48, 49, 50, 51, 52]
    '''
    deck = []
    for m in range(13):
        for n in range(4):
            deck += [(get_card(n, m))]
    return deck

def all_same_suit(cards):
    '''
    (list) -> bool
    
    Takes a list of cards between 1 and 52 as argument, and returns True if all
    cards in the list are of the same suit, and False otherwise.
    
    >>> all_same_suit([1, 5, 9, 13])
    True
    
    >>> all_same_suit([11, 27, 47, 51])
    True
    
    >>> all_same_suit([11, 27, 47, 52])
    False
    
    >>> all_same_suit([7])
    False
    
    >>> all_same_suit([57])
    False
    
    >>> all_same_suit([11, 59])
    False
    '''
    if len(cards) > 1:
        for card1 in cards:
            for card2 in cards:
                if not(same_suit(card1, card2)) or not(52 >= card1 >= 1 or 52 >= card2 >= 1):
                    return False
        return True
    else:
        return False

def all_same_rank(cards):
    '''
    (list) -> bool
    
    Takes a list of cards between 1 and 52 as argument, and returns True if all
    cards in the list are of the same rank, and False otherwise.
    
    >>> all_same_rank([1])
    False
    
    >>> all_same_rank([4, 87])
    False
    
    >>> all_same_rank([29, 30, 31, 32])
    True
    
    >>> all_same_rank([29, 30, 31, 35])
    False
    '''
    if len(cards) > 1:
        for card1 in cards:
            for card2 in cards:
                if not(same_rank(card1, card2)) or not(52 >= card1 >= 1 or 52 >= card2 >= 1):
                    return False
        return True
    else:
        return False