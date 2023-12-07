#Author: Christine Yang-Dai
#Student no: 260990057

def add_vectors(v1, v2):
    '''(dict, dict) -> void
    
    Given two dictionaries representing vectors, it adds the second vector to the first one.
    This function is void, and it modifies only the first input dictionary.
    
    >>> v1 = {'a' : 1, 'b' : 1}
    >>> v2 = {'a' : 1, 'b' : 1}
    >>> add_vectors(v1, v2)
    >>> v1 == {'a' : 2, 'b' : 2}
    True
    
    >>> v2 = {}
    >>> add_vectors(v1, v2)
    >>> v1 == {'a' : 2, 'b' : 2}
    True
    
    >>> v2 = {'a' : 3, 'c' : 1, 'b' : 2}
    >>> add_vectors(v1, v2)
    >>> v1 == {'a' : 5, 'b' : 4, 'c' : 1}
    True
    
    >>> v1 = {}
    >>> v2 = {'a': 1}
    >>> add_vectors(v1, v2)
    >>> v1 == v2
    True
    '''
    #iterating through the keys of the second dictionary
    for key in v2: 
        #if the key is aldo in dict1, add the values of the key
        #when the key is not in dictionary1, set the value to 0
        v1[key] = v1.get(key, 0) + v2.get(key)
    
def sub_vectors(d1, d2):
    '''(dict, dict) -> dict
    
    Given two dictionaries representing vectors, it returns a dictionary which is the
    result of subtracting the second vector from the first one.
    This function does not modify any of the input dictionaries.
    
    >>> d1 = {'a' : 5, 'b': 4, 'c' : 1}
    >>> d2 = {'a': 3, 'c': 1, 'b': 2}
    >>> d = sub_vectors(d1, d2)
    >>> d == {'a': 2, 'b' : 2}
    True
    
    >>> d2 = d1
    >>> d = sub_vectors(d1, d2)
    >>> d == {}
    True
    >>> d1 == {'a' : 5, 'b': 4, 'c' : 1}
    True
    >>> d2 == d1
    True
    
    >>> d2 = {}
    >>> d = sub_vectors(d1, d2)
    >>> d == d1
    True
    
    >>> d = sub_vectors(d2, d1)
    >>> d == {'a' : -5, 'b': -4, 'c' : -1}
    True
    >>> d1 == {'a' : 5, 'b': 4, 'c' : 1}
    True
    >>> d2 == {}
    True
    '''
    difference_v = {}
        
    for key in tuple(d1) + tuple(d2):
        #substract the values for the keys with the same value
        #if the key is not in a dictionary, the value for that key is set to 0
        difference_v[key] = d1.get(key, 0) - d2.get(key, 0)

        #if the difference is 0
        if difference_v.get(key) == 0:
            #remove the key
            del difference_v[key]
    
    return difference_v

def merge_dicts_of_vectors(d1, d2):
    '''(dict, dict) -> dict
    
    Given two dictionaries containing values which are dictionaries representing vectors,
    the function modifies the first input by merging it with the second one. This means
    that if both dictionaries contain the same key, then in the merged dictionary that
    same key will map to the sum of the two vectors. Note that this is a void function
    and it modifies only the first input dictionary.
    
    >>> d1 = {'a_key' : {'sub_key1': 1}, 'b_key' : {'sub_key2': 2, 'sub_key3': 3}}
    >>> d2 = {'b_key' : {'sub_key4' : 4}}
    >>> merge_dicts_of_vectors(d1, d2)
    >>> d1
    {'a_key': {'sub_key1': 1}, 'b_key': {'sub_key2': 2, 'sub_key3': 3, 'sub_key4': 4}}
    
    >>> merge_dicts_of_vectors(d2, d1)
    >>> d2
    {'b_key': {'sub_key4': 8, 'sub_key2': 2, 'sub_key3': 3}, 'a_key': {'sub_key1': 1}}
    
    >>> d4 = {'empty_eg' : {'some_key' : 4}}
    >>> d3 = {}
    >>> merge_dicts_of_vectors(d3, d4)
    >>> d3 == d4
    True
    
    >>> d0 = {}
    >>> merge_dicts_of_vectors(d3, d0)
    >>> d3
    {'empty_eg': {'some_key': 4}}
    '''
    #when the first dictionnary is empty, we want to make it the 2nd dictionnary
    for key in d2:
        #if the key is also in dict1, add their values
        add_vectors(d1.get(key,{}), d2.get(key))
        
        #else, create the key in dict1 with its value in dict2
        if key not in d1:
            d1[key] = d2.get(key)

def get_dot_product(v1, v2):
    '''(dict, dict) -> num
    
    Given two dictionaries representing vectors, returns the dot product of the two
    vectors.
    
    >>> v1 = {'a': 1, 'c': 2, 'b': 3}
    >>> v2 = {'a': 1, 'c': 5, 'b': 7}
    >>> get_dot_product(v1, v2)
    32
    
    >>> v3 = {'a' : 1, 'b': 1}
    >>> v4 = {'c': 1}
    >>> get_dot_product(v3, v4)
    0
    
    >>> v5 = {'a': -1.0, 'c': -2.0, 'b': 3.0}
    >>> v6 = {'a': 4.0, 'c': 0.0, 'b': -8.0}
    >>> get_dot_product(v5, v6)
    -28.0
    '''
    dot_product = 0
    
    for key in v1:
        dot_product += v1.get(key) * v2.get(key, 0) #formula for dot product
        
    return dot_product
    
def get_vector_norm(v):
    '''(dict) -> float
    
    Given a dictionary representing a vector, returns the norm of such vector.
    
    >>> v1 = {'a' : 2, 'b': -3}
    >>> round(get_vector_norm(v1), 3)
    3.606
    
    >>> v2 = {'a': -2, 'c': 3, 'b': 5}
    >>> round(get_vector_norm(v2), 3)
    6.164
    
    >>> v3 = {'a': 0, 'b': -2}
    >>> get_vector_norm(v3)
    2.0
    '''
    vector_norm_squared = 0
    
    for key in tuple(v):
        vector_norm_squared += v.get(key)**2 #the sum of the squared vectors
    
    return vector_norm_squared ** (0.5) #same as square root

def normalize_vector(v):
    '''(dict) -> Void or dict
    
    Given a dictionary representing a vector, the function modifies the dictionary by
    dividing each value by the norm of the vector. If the input vector has a norm of
    zero, then do not modify the vector
    
    >>> v1 = {'a' : 2, 'b': -3}
    >>> normalize_vector(v1)
    >>> round(v1['a'], 3)
    0.555
    >>> round(v1['b'], 3)
    -0.832
    
    >>> v2 = {'a': 0, 'c': 0, 'b': 0}
    >>> normalize_vector(v2)
    >>> v2
    {'a': 0, 'c': 0, 'b': 0}
    
    >>> v3 = {'a': 0, 'b': -2}
    >>> normalize_vector(v3)
    >>> v3
    {'a': 0.0, 'b': -1.0}
    '''
    norm = get_vector_norm(v)
    
    try:
        for key in v:
            v[key] = v[key]/norm # the formula for normalizing the vector
    except ZeroDivisionError:
        pass #if the norm is zero, do nothing