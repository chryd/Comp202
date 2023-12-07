#Author: Christine Yang-Dai
#Student no: 260990057

from random import *
from card2 import *

def draw(hand, top_discard_card):
    '''
    (list, int) -> str
    
    Takes a list of the cards in the player’s hand as argument, as well as the card currently at
    the top of the discard pile (if there is no card in the discard pile, None is given instead).
    Returns either 'stock' or 'discard' at random (unless there is no top card in the discard
    pile, in which case only 'stock' is returned).
    
    >>> seed(1)
    >>> randint(0, 1)
    0
    >>> seed(1)
    >>> draw([23, 46, 9, 10], 2)
    'discard'
    
    >>> seed(1)
    >>> draw([23, 46, 9, 10], None)
    'stock'
    
    >>> seed(0)
    >>> randint(0, 1)
    1
    >>> seed(0)
    >>> draw([35, 28, 1, 23], 52)
    'stock'
    '''
    
    
    if top_discard_card in range(52):
        action_int = randint(0, 1)
    else:
        action_int = 1

    if action_int == 0:
        return 'discard'
    else:
        return 'stock'

def discard(hand):
    '''
    (list) -> int
    
    Takes a list of the cards in the player’s hand as argument, and returns a random
    card in the hand.
    
    >>> seed(1)
    >>> randint(0, 4)
    1
    >>> seed(1)
    >>> discard([1, 2, 3, 4])
    2
    
    >>> seed(2)
    >>> randint(0, 4)
    0
    >>> seed(2)
    >>> discard([49, 15, 2, 32])
    49
    
    >>> seed(7)
    >>> randint(0, 5)
    2
    >>> seed(7)
    >>> discard([34, 9, 45, 7, 12])
    45
    '''
    return hand[randint(0, len(hand) - 1)]