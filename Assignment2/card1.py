HEARTS, DIAMONDS, CLUBS, SPADES = 0, 1, 2, 3

TWO, THREE, FOUR, FIVE, SIX, SEVEN = 0, 1, 2, 3, 4, 5
EIGHT, NINE, TEN, JACK, QUEEN, KING, ACE = 6, 7, 8, 9, 10, 11, 12

def get_suit(card):
    return (card-1) % 4

def get_rank(card):
    return ((card -1) // 4) % 13

def same_rank(card1, card2):
    return get_rank(card1) == get_rank(card2)

def same_suit(card1, card2):
    return get_suit(card1) == get_suit(card2)

def same_color_suit(card1, card2):
    suit1 = get_suit(card1)
    suit2 = get_suit(card2)
    both_red = (suit1 == HEARTS or suit1 == DIAMONDS) and (suit2 == HEARTS or suit2 == DIAMONDS)
    both_black = (suit1 == CLUBS or suit1 == SPADES) and (suit2 == SPADES or suit2 == CLUBS) 
    return both_red or both_black
