#Author: Christine Yang-Dai
#Student no: 260990057
from vectors_utils import *

def get_semantic_descriptor(word, sentence):
    '''(str, list) -> dict
    
    Given a string w representing a single word and a list s representing all
    the words in a sentence, returns a dictionary representing the semantic
    descriptor vector of the word w computed from the sentence s.
    
    >>> s1 = ['a2', 'a2', 'b1', 'c1', 'd2', 'd2', 'test']
    >>> desc1 = get_semantic_descriptor('test', s1)
    >>> desc1
    {'a2': 2, 'b1': 1, 'c1': 1, 'd2': 2}
    
    >>> get_semantic_descriptor('not_present', s1)
    {}
    
    >>> s3 = ['a', 'sentence', 'for', 'a', 'test' ]
    >>> get_semantic_descriptor('sentence', s3)
    {'a': 2, 'for': 1, 'test': 1}
    '''
    semantic_descriptor = {}
    
    #do the loop only if the word is in the sentence
    if word in sentence:
        for a_word in sentence:
            #for the words which are not the sentence
            if a_word != word:
                #the value for the word is the number of time the word appears
                semantic_descriptor[a_word] = sentence.count(a_word)
    
    return semantic_descriptor

def get_all_semantic_descriptors(text):
    '''(list) -> dict
    
    Takes as input a list of lists representing the words in a text, where each sentence in
    a text is represented by a sublist of the input list. The function returns a dictionary
    d such that for every word w that appears in at least one of the sentences, d[w] is
    itself a dictionary which represents the semantic descriptor vector of w.
    
    >>> s = [['a', 'a', 'b', 'c', 'd', 'd', 'test'], ['a', 'sentence', 'for', 'a', 'test' ]]
    >>> d = get_all_semantic_descriptors(s)
    >>> d['a']
    {'b': 2, 'c': 2, 'd': 4, 'test': 4, 'sentence': 2, 'for': 2}
    >>> d['test']
    {'a': 4, 'b': 1, 'c': 1, 'd': 2, 'sentence': 1, 'for': 1}
    
    >>> s = [['my', 'first', 'sentence'], ['second','sentence']]
    >>> d = get_all_semantic_descriptors(s)
    >>> d['sentence']
    {'my': 1, 'first': 1, 'second': 1}
    
    >>> s = [['draw', 'paint', 'walk', 'paint']]
    >>> get_all_semantic_descriptors(s)
    {'draw': {'paint': 2, 'walk': 1}, 'paint': {'draw': 2, 'walk': 2}, 'walk': {'draw': 1, 'paint': 2}}
    '''
    all_semantic_descriptors = {}
    
    for sentence in text:
        sentence_semantic_descriptors = {}
        
        for word in sentence:
            #skip this loop if the word has already been added
            if word not in sentence_semantic_descriptors:
                #adding in the dictionary sentence_semantic_descriptors the words as key
                #and the corresponding semantic descriptor as value
                d = get_semantic_descriptor(word, sentence)
                sentence_semantic_descriptors[word] = d
        
                for i in range(sentence.count(word) - 1):
                    #if a word is repeated i times in the sentence
                    #the same semantic_descriptors appears i times and need to be multiplied by i
                    add_vectors(sentence_semantic_descriptors.get(word), d)
                
        #merge the semantic_descriptors of the sentences to the main dict
        merge_dicts_of_vectors(all_semantic_descriptors, sentence_semantic_descriptors)
    
    return all_semantic_descriptors

def get_cos_sim(v1, v2):
    '''(dict, dict) -> float

    Given two dictionaries representing similarity descriptor vectors, returns the cosine
    similarity between the two.
    
    >>> round(get_cos_sim({'a': 2, 'b': 1}, {'c': 2, 'b': 2}), 2)
    0.32
    
    >>> get_cos_sim({'a': 1, 'b': 0}, {'c': 0, 'b': 0})
    0
    
    >>> s = [['a', 'a', 'b', 'c', 'd', 'd', 'test'], ['a', 'sentence', 'for', 'a', 'test' ]]
    >>> d = get_all_semantic_descriptors(s)
    >>> v1 = d['test']
    >>> v2 = d['d']
    >>> round(get_cos_sim(v1, v2), 4)
    0.7715
    
    >>> s = [['my', 'first', 'sentence'], ['second','sentence']]
    >>> d = d = get_all_semantic_descriptors(s)
    >>> v1 = d['second']
    >>> v2 = d['sentence']
    >>> round(get_cos_sim(v1, v2), 4)
    0.0
    '''
    try:
        return get_dot_product(v1, v2) / (get_vector_norm(v1) * get_vector_norm(v2)) #formula for cos sim
    except ZeroDivisionError:
        #this mean one of the vectors is empty
        return 0    #and no key can be similar within an empty vector

def get_euc_sim(v1, v2):
    '''(dict, dict) -> float

    Given two dictionaries representing similarity descriptor vectors, returns the similarity
    between the two using the negative euclidean distance.
    
    >>> get_euc_sim({"a": 5, "b": 8, "c": 3}, {"b": 4, "c": 3, "a": 2})
    -5.0
    
    >>> get_euc_sim({"a": 5, "b": 8, "c": 3}, {"b": 8, "c": 3, "a": 5})
    -0.0
    
    >>> get_euc_sim({"a": 0, "b": 0, "c": 0}, {"b": 0, "c": 0, "a": 0})
    -0.0
    
    >>> s = [['a', 'a', 'b', 'c', 'd', 'd', 'test'], ['a', 'sentence', 'for', 'a', 'test' ]]
    >>> d = get_all_semantic_descriptors(s)
    >>> v1 = d['d']
    >>> v2 = d['test']
    >>> round(get_euc_sim(v1, v2), 4)
    -3.4641
    '''
    return -(get_vector_norm(sub_vectors(v1, v2))) #formula for euc_sim

def deep_copy_norm(v):
    '''(dict) -> dict
    To create a deep copy of a normalized dictionary.
    
    >>> v = {"a": 5, "b": 8, "c": 3}
    >>> c = deep_copy_norm(v)
    >>> round(c['a'], 3)
    0.505
    >>> v == {"a": 5, "b": 8, "c": 3}
    True
    
    >>> v1 = {'a' : 2, 'b': -3}
    >>> c = deep_copy_norm(v1)
    >>> round(c['a'], 3)
    0.555
    >>> round(v1['a'], 3)
    2
    
    >>> round(c['b'], 3)
    -0.832
    >>> round(v1['b'], 3)
    -3
    '''
    copy_v = {}
    
    for k in v:
        copy_v[k] = v.get(k)
    
    normalize_vector(copy_v)
    
    return copy_v

def get_norm_euc_sim(v1, v2):
    '''(dict, dict) -> float

    Given two dictionaries representing similarity descriptor vectors, returns the
    similarity between the two using the negative euclidean distance between the normalized vectors.
    
    >>> get_norm_euc_sim({"a": 5, "b": 8, "c": 3}, {"b": 4, "c": 3, "a": 2})
    -0.294410754924937
    
    >>> get_norm_euc_sim({"a": 0, "b" : 0}, {"a" : 0, "b" : 0})
    -0.0
    
    >>> s = [['a', 'a', 'b', 'c', 'd', 'd', 'test'], ['a', 'sentence', 'for', 'a', 'test' ]]
    >>> d = get_all_semantic_descriptors(s)
    >>> v1 = d['test']
    >>> v2 = d['d']
    >>> round(get_norm_euc_sim(v1, v2), 4)
    -0.676
    >>> v1 == d['test']
    True
    '''
    return get_euc_sim(deep_copy_norm(v1), deep_copy_norm(v2))  #formula for norm_euc_sim