#Author: Christine Yang-Dai
#Student no: 260990057

from card2 import *

def calculate_winner(points):
    '''
    (list) -> list
    
    Takes a list of scores (integers) as argument, and returns a list containing
    the indices of the list corresponding to the lowest points in the points list.
    
    >>> calculate_winner([12, 254, 3, 3, 45])
    [2, 3]
    
    >>> calculate_winner([12, 254, 3, 45])
    [2]
    '''
    indice = []
    for i in range(len(points)):
        if points[i] == min(points):
            indice += [i]
    return indice

def calculate_round_points(hand):
    '''
    (list) -> int
    
    Takes a player’s hand (list of cards) as argument, and returns the point value of that hand.
    Points for a hand are calculated depending on the ranks of the cards in the hand:
        An Ace is 1 point;
        Twos through Tens are their numeric value;
        Jack/Queen/King are all 10 points;
    
    >>> calculate_round_points([36, 38, 43, 46])
    40
    
    >>> calculate_round_points([1, 5, 9, 13, 17, 21, 25, 29, 33, 52])
    55
    
    >>> calculate_round_points([29, 50, 49, 35])
    21
    '''
    points = 0
    for card in hand:
        if get_rank(card) in [0, 1, 2, 3, 4, 5, 6, 7]:
            points += get_rank(card) + 2
        elif get_rank(card) in [8, 9, 10, 11]:
            points += 10
        else:
            points += 1
    return points

def is_valid_group(cards):
    return (len(cards) >= 3 and all_same_rank(cards))
    
def is_valid_sequence(cards):
    if (len(cards) >= 3 and all_same_suit(cards)):
        cards.sort()
        for i in range(len(cards)):
            if cards[i] != cards[-1]:
                if get_rank(cards[i]) > get_rank(cards[i + 1]):
                    return False
        return True
    else:
        return False
