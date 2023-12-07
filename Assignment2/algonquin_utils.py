#Author: Christine Yang_Dai
#Student no: 260990057

CONSONANTS = "bcdghkmnpstwyzj"
VOWELS = "aeio"
VOWELS_WITH_ACCENT = "àèìò"
PUNCTUATION = ',;:.?!-'
DIPHTHONGS = ['aw', 'ay', 'ew', 'ey', 'iw', 'ow']

punctuation_space = PUNCTUATION + ' '

def is_valid_consonant(char):
    '''
    (str) -> bool
    
    Given a string, determines if it’s a single character representing a valid
    consonant in Algonquin. This function should not be case sensitive. Please
    note that "dj" is not a single character.
    
    >>> is_valid_consonant('')
    False
    
    >>> is_valid_consonant('1')
    False
    
    >>> is_valid_consonant('a')
    False
    
    >>> is_valid_consonant('K')
    True
    
    >>> is_valid_consonant('l')
    False
    
    >>> is_valid_consonant('bc')
    False
    '''
    return ((char.lower() in CONSONANTS) and (len(char) == 1))

def is_valid_vowel(char):
    '''
    (str) -> bool
    
    Given a string, determines if it’s a single character representing
    a valid vowel in Algonquin. This function should not be case sensitive.
    
    >>> is_valid_vowel(' ')
    False
    
    >>> is_valid_vowel('')
    False
    
    >>> is_valid_vowel('1')
    False
    
    >>> is_valid_vowel('k')
    False
    
    >>> is_valid_vowel('A')
    True
    
    >>> is_valid_vowel('à')
    True
    
    >>> is_valid_vowel('ae')
    False
    '''
    return (((char.lower() in VOWELS) or (char.lower() in VOWELS_WITH_ACCENT)) and (len(char) == 1))

def is_valid_single_word(word):
    '''
    (char) -> bool

    Given a string, determines if it contains a single word made
    up by valid letters in Algonquin. This function should not
    be case sensitive.
    
    >>> is_valid_single_word('ca')
    True
    
    >>> is_valid_single_word('good morning')
    False
    
    >>> is_valid_single_word('dAykO')
    True
    
    >>> is_valid_single_word('sèhew')
    True
    
    >>> is_valid_single_word('far')
    False
    '''
    
    for char in word:
        not_valid_char = not(is_valid_consonant(char) or is_valid_vowel(char))
        if not_valid_char:
            return False
    return True

def sign_in_phrase(phrase):
    '''
    (str) -> bool
    
    Verify is there is a punctuation or space in the given string.
    Return True if there is, False otherwise.
    
    >>> sign_in_phrase("!.?yes")
    True
    
    >>> sign_in_phrase("yes")
    False
    
    >>> sign_in_phrase(" ")
    True
    
    >>> sign_in_phrase("")
    False
    '''
    for sign in punctuation_space:
        if sign in phrase:
            return True
    return False

def is_valid_phrase(phrase):
    '''
    (str) ->  bool

    Given a string, determines if it contains only valid letters in Algonquin,
    accepted punctuation marks, or space characters. This function should not
    be case sensitive.
    
    >>> is_valid_phrase('Mino Kigijebawan')
    True
    
    >>> is_valid_phrase('Anin tash epideg?')
    True
    
    >>> is_valid_phrase('falalalala')
    False
    
    >>> is_valid_phrase('???')
    True
    
    >>> is_valid_phrase(' ')
    False
    '''
    words = []
    i = 0
    f = len(phrase)
    
    if phrase == " ":
        return False
    
    if sign_in_phrase(phrase):
        for n in range(len(phrase)):
            if phrase[n] in punctuation_space:
                f = n
                words += [phrase[i:f]]
                i = n + 1
            
        if phrase[-1] not in punctuation_space:
            words += [phrase[i:(len(phrase))]]
    else:
        words = [phrase[i:f]]
        
    for word in words:
        if not(is_valid_single_word(word)):
            return False
    return True
