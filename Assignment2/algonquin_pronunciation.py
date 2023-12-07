#Author: Christine Yang_Dai
#Student no: 260990057

from algonquin_utils import *

def get_consonant_pronunciation(algonquin):
    '''
    (str) -> str
    
    Given a string, if it is a valid consonant return its pronunciation, 
    otherwise return an empty string.
    
    >>> get_consonant_pronunciation('J')
    'GE'
    
    >>> get_consonant_pronunciation('dj')
    'J'
    
    >>> get_consonant_pronunciation('f')
    ''
    
    >>> get_consonant_pronunciation('C')
    'C'    
    '''
    if algonquin.lower() == 'dj':
        return 'J'
    elif is_valid_consonant(algonquin):
        if algonquin.lower() == 'j':
            return 'GE'
        else:
            return algonquin.upper()
    else:
        return ''

def get_vowel_pronunciation(algonquin):
    '''
    (str) -> str
    
    Given a string, if it is a valid vowel return its pronunciation,
    otherwise return an empty string.
    
    >>> get_vowel_pronunciation("À")
    'A'
    
    >>> get_vowel_pronunciation("è")
    'E'
    
    >>> get_vowel_pronunciation("o")
    'U'
    
    >>> get_vowel_pronunciation("i")
    'I'
    
    >>> get_vowel_pronunciation("oi")
    ''
    '''
    a_list = ['a', 'à']
    e_list = ['e', 'è']
    
    if is_valid_vowel(algonquin):
        if algonquin.lower() in a_list :
            return 'A'
        elif algonquin.lower() in e_list:
            return 'E'
        elif algonquin.lower() == 'ì':
            return 'EE'
        elif algonquin.lower() == 'o':
            return 'U'
        elif algonquin.lower() == 'ò':
            return 'O'
        else:
            return algonquin.upper()
    else:
        return ''

def get_diphthong_pronunciation(algonquin):
    '''
    (str) -> str
    
    Given a string, if it is a valid diphthon return its pronunciation,
    otherwise return an empty string. For the sake of implification,
    'dj' is cpnsidered a diphthong.
    
    >>> get_diphthong_pronunciation("aw")
    'OW'
    
    >>> get_diphthong_pronunciation("eY")
    'AY'
    
    >>> get_diphthong_pronunciation("IW")
    'EW'
    
    >>> get_diphthong_pronunciation("oi")
    ''
    '''
    
    if algonquin.lower() in DIPHTHONGS:
        if algonquin.lower() == 'aw':
            return 'OW'
        elif algonquin.lower() == 'ay':
            return 'EYE'
        elif algonquin.lower() == 'ew':
            return 'AO'
        elif algonquin.lower() == 'ey':
            return 'AY'
        elif algonquin.lower() == 'iw':
            return 'EW'
        elif algonquin.lower() == 'dj':
            return 'J'
        else:
            return algonquin.upper()
    else:
        return ''

def get_word_pronunciation(algonquin):
    '''
    (str) -> str
    
    Given a string, if it is a valid word return its pronunciation,
    otherwise return an empty string.

    >>> get_word_pronunciation('kigijebawan')
    'KIGIGEEBOWAN'

    >>> get_word_pronunciation('Wìdòkwishnàng')
    'WEEDOKWISHNANG'

    >>> get_word_pronunciation('Kichi-mìgwech')
    ''
    '''
    algonquin = algonquin.lower()
    
    if is_valid_single_word(algonquin):
        pronunciation = ''
        a = 0
        while a < (len(algonquin)):
            if algonquin[a] in CONSONANTS:
                if algonquin[a: a + 2] == 'dj':
                    pronunciation += get_consonant_pronunciation(algonquin[a: a + 2])
                    a += 2
                else:
                    pronunciation += get_consonant_pronunciation(algonquin[a])
                    a += 1
            else:
                if algonquin[a: a + 2] in DIPHTHONGS:
                    pronunciation += get_diphthong_pronunciation(algonquin[a: a + 2])
                    a += 2
                else:
                    pronunciation += get_vowel_pronunciation(algonquin[a])
                    a += 1
        return pronunciation
    else:
        return ''

def tokenize_sentence(algonquin):
    '''
    (str) -> list
    
    Given a string, if it is a valid phrase, break it down into strings representing either single words
    or a sequence of punctuation marks and space characters. The function returns a list containing all
    these strings. If the input string is not a valid phrase, then return an empty list.
    
    >>> tokenize_sentence('falalalala')
    []
    
    >>> tokenize_sentence('Kwey')
    ['Kwey']
    
    >>> tokenize_sentence('Kin tash anin ejipimadizin?')
    ['Kin', ' ', 'tash', ' ', 'anin', ' ', 'ejipimadizin', '?']
    
    >>> tokenize_sentence('mino kijigad')
    ['mino', ' ', 'kijigad']
    
    >>> tokenize_sentence('Kwey, mino kijigad')
    ['Kwey', ', ', 'mino', ' ', 'kijigad']
    '''
    token_list = []
    x = 0
    y = len(algonquin)
    
    if is_valid_phrase(algonquin):
        
        if sign_in_phrase(algonquin):
            k = 0 #index of the characters
            
            while k < (len(algonquin)):
                if algonquin[k] in punctuation_space:    #which signal the end of a word
                    if algonquin[k] in '- ' :
                        #adding the word before the sign and the sign
                        token_list += [algonquin[x:k], algonquin[k]]
                        x = k + 1    #where the next word start
                    else:
                        #adding the word before the sign and the sign followed by a space
                        token_list += [algonquin[x:k], algonquin[k: k + 2]]
                        x = k + 2    #where the next word start
                        k += 1    #to skip the space following the sign
                k += 1    #to the next character
                
            if algonquin[-1] not in punctuation_space:
                #if the sentence does not end on a sign, it marks the end
                token_list += [algonquin[x:(len(algonquin))]]
        else:
            token_list = [algonquin[x:y]]    #the whole sentence is just a word
            
        return token_list
    
    else:
        return []

def get_sentence_pronunciation(algonquin):
    '''
    (str) -> str
    
    Given a string, if it is a valid string return its pronunciation, otherwise
    return an empty string.
    
    >>> get_sentence_pronunciation("Miigwechwewin Kichi-mìgwech")
    'MIIGWECHWAOIN KICHI-MEEGWECH'
    
    >>> get_sentence_pronunciation("Anin eji-pimadizin?")
    'ANIN EGEI-PIMADIZIN?'
    
    >>> get_sentence_pronunciation("maDjAShiN")
    'MAJASHIN'
    
    >>> get_sentence_pronunciation("do re mi fa sol la si")
    ''
    '''
    new_pronunciation = ''
    if is_valid_phrase(algonquin):
        for term in tokenize_sentence(algonquin):
            if is_valid_single_word(term):
                new_pronunciation += get_word_pronunciation(term)
            else:
                new_pronunciation += term
        return new_pronunciation
    else:
        return ''