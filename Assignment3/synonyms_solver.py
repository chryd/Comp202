#Author: Christine Yang-Dai
#Student no: 260990057
from similarity_measures import *
from file_processing import *
import matplotlib.pyplot as plt
import doctest

def most_sim_word(word, choices, semantic_descriptors, similarity_fn):
    '''(str, list, dict, function) -> str
    
    This function takes four inputs: a string word, a list of strings choices, and a dictionary
    semantic_descriptors which is built according to the requirements for get_all_semantic_descriptors,
    and a similarity function similarity_fn. The function returns the element of choices which has
    the largest semantic similarity to word, with the semantic similarity computed using the data in
    semantic_descriptors and the similarity function similarity_fn. The similarity function is a function
    which takes in two sparse vectors stored as dictionaries and returns a float.
    
    >>> choices = ['flower', 'gold', 'horse']
    >>> p = {'grow' : 3, 'green' : 5, 'garden' : 4}
    >>> f = {'grow' : 2, 'garden' : 5, }
    >>> g = {'mine' : 3, 'yellow' : 5, 'shine' : 8}
    >>> h = {'race' : 4, 'queen' : 2}
    >>> sem_descs = {'plant' : p, 'flower' : f, 'gold' : g, 'horse' : h}
    >>> most_sim_word('plant', choices, sem_descs, get_cos_sim)
    'flower'
    
    >>> choices = ['b', 'c']
    >>> a = {'x' : 4, 'y' : 3, 'z' : 1}
    >>> b = {'m' : 3, '' : 1}
    >>> c = {'x' : 2, 'z': 4}
    >>> sem_descs = {'a' : a, 'b' : b, 'c' : c}
    >>> most_sim_word('a', choices, sem_descs, get_euc_sim)
    'c'
    
    >>> choices = ['d', 'c']
    >>> a = {'x' : 4, 'y' : 3, 'z' : 1}
    >>> b = {'m' : 3, '' : 1}
    >>> c = {'x' : 2, 'z': 4}
    >>> sem_descs = {'a' : a, 'b' : b, 'c' : c}
    >>> most_sim_word('a', choices, sem_descs, get_euc_sim)
    'c'
    '''
    #the list for the similarity values
    sim_values = []
    
    for choice in choices:
        try:
            #add the value given by the function to the list
            sim_values += [similarity_fn(semantic_descriptors[word], semantic_descriptors[choice])]
        except:
            #when the value cannot be processed, returns float('-inf')
            sim_values += [float('-inf')]
            
    #return the word mapped to the maximum similarity value
    return choices[sim_values.index(max(sim_values))]

def run_sim_test(filename, semantic_descriptors, similarity_fn):
    '''(str, dict, function) -> float
    
    This function takes three inputs: a string filename, a dictionary semantic_descriptors,
    and a function similarity_fn. The string is the name of a file in the same format as test.txt.
    The function returns the percentage (i.e., float between 0.0 and 100.0) of questions on which
    most_sim_word guesses the answer correctly using the semantic descriptors stored in semantic_descriptors,
    and the similarity function similarity_fn.
    
    >>> descriptors = build_semantic_descriptors_from_files(['animal_farm.txt'])
    >>> run_sim_test('test.txt', descriptors, get_cos_sim)
    47.5
    
    >>> descriptors = build_semantic_descriptors_from_files(['test.txt'])
    >>> run_sim_test('test.txt', descriptors, get_norm_euc_sim)
    15.0
    >>> run_sim_test('test.txt', descriptors, get_euc_sim)
    20.0
    '''
    #we start with no good answer and no answer at all
    good_answers = 0
    total_answers = 0
    
    #opening the file
    text = open(filename, 'r')
    
    #for each line
    for line in text:
        #strip the '\n'
        line = line.strip('\n')
        #split between each space
        line_list = line.split(' ')
        #computer is taking a guess with the fct most_sim_word
        guess = most_sim_word(line_list[0], line_list[2:], semantic_descriptors, similarity_fn)
        
        #if it is the good answer, calculate +1 good answer
        if guess == line_list[1]:
            good_answers += 1
            
        #add to the total answers answered   
        total_answers += 1
    
    #close the text
    text.close()
    
    return round(good_answers / total_answers * 100, 1)

def generate_bar_graph(functions, filename):
    '''(list, str) -> Void

    Given a list of similarity functions and a string filename (which is the name of a file in the same
    format as test.txt) generates a bar graph (using matplotlib) where the performance of each function
    on the given file test is plotted. The graph is saved in a file named synonyms_test_results.png.
    '''
    #values on the y axis
    y = []
    #values on the x axis
    x = []
    
    d = build_semantic_descriptors_from_files(['swanns_way.txt', 'war_and_peace.txt'])
    #for each fct in the list
    for sim_fct in functions:
        #the value of y is the result of the test
        y += [run_sim_test(filename, d, sim_fct)]
        #associated to the name of the fct
        x += [sim_fct.__name__]
    
    #plot a bar graph with variables x and y
    plt.bar(x, y)
    #save it in a file under the name synonyms_test_results.png
    plt.savefig("synonyms_test_results.png")