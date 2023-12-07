#Author: Christine Yang-Dai
#Student no: 260990057
from similarity_measures import *

def get_sentences(t):
    '''(str) -> list
    
    Given a string, returns a list of strings each representing one of the sentences from
    the input string.
    
    >>> text = "This is the first sentence. This is the second one."
    >>> get_sentences(text)
    ['This is the first sentence', 'This is the second one']
    
    >>> t = "What?! No way! I can't believe it."
    >>> get_sentences(t)
    ['What', 'No way', "I can't believe it"]
    
    >>> t = "She felt a presence behind her. Was it her imagination? It must be..."
    >>> get_sentences(t)
    ['She felt a presence behind her', 'Was it her imagination', 'It must be']
    
    >>> t = "Oh, no! I made a typo,"
    >>> get_sentences(t)
    ['Oh, no', 'I made a typo,']
    '''
    for i in range(len(t)):
        #if i is in the range, and there is a punctuation followed by a space
        if (i < len(t) - 1) and ((t[i] + t[i + 1]) in ('. ', '! ', '? ')):
            #the characters is replaced by .. (to avoid index error)
            t = t.replace(t[i] + t[i + 1], "..")
        elif t[i] in '!?': #else, punctuation different from '.' are transformed into '.'
            t = t.replace(t[i], ".")
    
    #split the text into a list of words seperated at .
    sentence_list = t.split(".")
    
    #empty list are added when 2 punctuations are following each other (... or ?! for instance)
    #removing all empty strings
    for i in range(sentence_list.count('')):
        sentence_list.remove('')
    
    return sentence_list

def get_word_breakdown(text):
    '''(str) -> list
    
    Given a string returns a 2D lists of strings. Each sublist contains a strings
    representing words from each sentence.
    
    >>> text = "This is the first sentence. This is the second one."
    >>> w = get_word_breakdown(text)
    >>> w
    [['this', 'is', 'the', 'first', 'sentence'], ['this', 'is', 'the', 'second', 'one']]
    
    >>> t = "WHAT?! NO WAY! I can't believe this."
    >>> get_word_breakdown(t)
    [['what'], ['no', 'way'], ['i', 'can', 't', 'believe', 'this']]
    
    >>> t = "Oh, nO--I MadE a tYpO,"
    >>> get_word_breakdown(t)
    [['oh', 'no', 'i', 'made', 'a', 'typo']]
    
    >>> t = '"Heavens! what a virulent attack!" replied the prince.'
    >>> get_word_breakdown(t)
    [['heavens'], ['what', 'a', 'virulent', 'attack'], ['replied', 'the', 'prince']]
    
    >>> l = "HERE IS A LIST OF RANDOM THINGS: paper; Kat's cat; city; St-Laurent; etc."
    >>> get_word_breakdown(l)
    [['here', 'is', 'a', 'list', 'of', 'random', 'things', 'paper', 'kat', 's', 'cat', 'city', 'st', 'laurent', 'etc']]
    '''
    #putting everthing in lower case from the start
    text = text.lower()
    
    #the general 2D list
    word_breakdown = []
    
    for sentence in get_sentences(text):
        for char in sentence:
            #if a punctuation or space marking the end of a word appears
            if char in (',','-',':',';','"',"'",'\n','\t'):
                #replacing all punctuations by spaces
                sentence = sentence.replace(char, " ")
        
        #split the sentence into a list of the words
        word_in_sentence = sentence.split()
              
        #when 2 punctuations follow each other, an empty space is added
        #remove all empty elements
        for i in range(word_in_sentence.count('')):
            word_in_sentence.remove('')
        
        #the list of the words in each sentence is added to the main list
        word_breakdown.append(word_in_sentence)
        
    return word_breakdown

def build_semantic_descriptors_from_files(files):
    '''(list) -> list
    
    Given a list of file names (strings) as input returns a dictionary of the semantic
    descriptors of all the words in the files received as input, with the files treated
    as a single text.
    
    >>> d = build_semantic_descriptors_from_files(['animal_farm.txt'])
    >>> d['animal']['no']
    3
    >>> d['brothers']
    {'weak': 1, 'or': 2, 'strong': 1, 'clever': 1, 'simple': 1, 'we': 1, 'are': 1, 'all': 1}
    
    >>> d = build_semantic_descriptors_from_files(['animal_farm.txt', 'alice.txt'])
    >>> len(d['must'])
    29
    >>> d['man']['all']
    1
    >>> d['man']['must']
    1
    '''    
    text = ''
    #for each file in the list of files
    for filename in files:
        #create a file object to read
        fobj = open(filename, "r", encoding="utf-8")
        #read the file
        text += fobj.read()
        #close the file
        fobj.close()
    
    return get_all_semantic_descriptors(get_word_breakdown(text))