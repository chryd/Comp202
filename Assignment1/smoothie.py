#Author: Christine Yang-Dai
#This program serves as an ordering system for smoothies

#variables
SMOOTHIE1_NAME = 'Apple'
SMOOTHIE2_NAME = 'Banana'
SMOOTHIE3_NAME = 'Strawberry'
SMOOTHIE4_NAME = 'Onion Toffee'

SMOOTHIE1_COST = 3.99
SMOOTHIE2_COST = 4.49
SMOOTHIE3_COST = 5.69
SMOOTHIE4_COST = 9.99

SIZE1_NAME = 'small'
SIZE2_NAME = 'medium'
SIZE3_NAME = 'large'
SIZE4_NAME = 'galactic'

SIZE1_COST = -2.00
SIZE2_COST = 0.0
SIZE3_COST = 2.0
SIZE4_COST = 100.0

TOPPING1_NAME = 'no topping'
TOPPING2_NAME = 'caramel'
TOPPING3_NAME = 'coffee'
TOPPING4_NAME = 'candy'

TOPPING1_COST = 0.0
TOPPING2_COST = 1.0
TOPPING3_COST = 1.0
TOPPING4_COST = 1.0

#This function prints all options and return the choice of the user.
def pose_question_with_costs(question, option1, cost1, option2, cost2, option3, cost3, option4, cost4):
    '''
    (str, str, float, str, float, str, float, str, float) -> str or NoneType
    
    The function print the greeting and each option and their respective cost.
    Then it takes in the user's option. It prints a confirmation of the option.
    Then it returns the user's option.
    If the choice is invalid, the function prints an empty string.
    
    >>> pose_question_with_costs('Which smoothie would you like?', 'Apple', 3.99, 'Banana', 4.49, 'Strawberry', 5.69, 'Onion Toffee', 9.99)
        Which smoothie would you like?
        1)  $ 3.99   Apple
        2)  $ 4.49   Banana
        3)  $ 5.69   Strawberry
        4)  $ 9.99   Onion Toffee
        Your choice (1-4): 1
        You have selected Apple.
        'Apple'
        
    >>> pose_question_with_costs('Which size do you want?', 'small', -2.00, 'medium', 0.0, 'large', 2.0, 'galactic', 100.0)
        Which size do you want?
        1)  $ -2.0   small
        2)  $ 0.0    medium
        3)  $ 2.0    large
        4)  $ 100.0      galactic
        Your choice (1-4): 3
        You have selected large.
        'large'
        
    >>> pose_question_with_costs('Which topping would you like?', 'no topping', 0.0, 'caramel', 1.0, 'coffee', 1.0, 'candy', 1.0)
        Which topping would you like?
        1)  $ 0.0    no topping
        2)  $ 1.0    caramel
        3)  $ 1.0    coffee
        4)  $ 1.0    candy
        Your choice (1-4): cat
         
    '''
    print(question)
    print('1)\t$', cost1, '\t', option1)
    print('2)\t$', cost2, '\t', option2)
    print('3)\t$', cost3, '\t', option3)
    print('4)\t$', cost4, '\t', option4)
    
    user_choice = input("Your choice (1-4): ")
    
    if ((user_choice !='1') and (user_choice !='2') and (user_choice !='3') and (user_choice !='4')):
        print(' ')
    else:
        user_choice = int(user_choice)
        
        if user_choice == 1:
            user_option = option1
        elif user_choice == 2:
            user_option = option2
        elif user_choice == 3:
            user_option = option3
        elif user_choice == 4:
            user_option = option4
        
        print('You have selected ' + user_option + '.')
            
        return user_option
    
#This function finds the subtotal for each parameter (smoothie type, size and topping)    
def subtotal_parameter(parameter, global_name1, global_name2, global_name3, global_cost1, global_cost2, global_cost3, global_cost4):
    '''
    (str, str, str, str, float, float, float, float) -> float
            
    Take in the parameter that the fonction is testing and compare it to its
    corresponding global variable. Return the corresponding cost.
            
    >>> subtotal_parameter(smoothie_type, SMOOTHIE1_NAME, SMOOTHIE2_NAME, SMOOTHIE3_NAME, SMOOTHIE1_COST, SMOOTHIE2_COST, SMOOTHIE3_COST, SMOOTHIE4_COST)
    5.69
            
    >>> subtotal_parameter(smoothie_size, SIZE1_NAME, SIZE2_NAME, SIZE3_NAME, SIZE1_COST, SIZE2_COST, SIZE3_COST, SIZE4_COST)
    -2.0
            
    >>> subtotal_parameter(topping, TOPPING1_NAME, TOPPING2_NAME, TOPPING3_NAME, TOPPING1_COST, TOPPING2_COST, TOPPING3_COST, TOPPING4_COST)
    0.0
    '''
    if parameter == global_name1:
        cost_parameter = global_cost1
    elif parameter == global_name2:
        cost_parameter = global_cost2
    elif parameter == global_name3:
        cost_parameter = global_cost3
    else:
        cost_parameter = global_cost4

    return cost_parameter

#This function calculate the subtotal of the order
def calculate_subtotal(smoothie_type, smoothie_size, topping):
    '''
    (str, str, str) -> float
    
    Take in type, size and topping of smoothie. Return the cost rounded to 2 decimals.
    
    >>> calculate_subtotal('Apple', 'small', 'no topping')
    1.99
    
    >>> calculate_subtotal('Onion Toffee', 'medium', 'candy')
    10.99
    
    >>> calculate_subtotal('Onion Toffee', 'galactic', 'coffee')
    110.99
    '''
    type_cost = subtotal_parameter(smoothie_type, SMOOTHIE1_NAME, SMOOTHIE2_NAME, SMOOTHIE3_NAME, SMOOTHIE1_COST, SMOOTHIE2_COST, SMOOTHIE3_COST, SMOOTHIE4_COST)
    size_cost = subtotal_parameter(smoothie_size, SIZE1_NAME, SIZE2_NAME, SIZE3_NAME, SIZE1_COST, SIZE2_COST, SIZE3_COST, SIZE4_COST)
    topping_cost = subtotal_parameter(topping, TOPPING1_NAME, TOPPING2_NAME, TOPPING3_NAME, TOPPING1_COST, TOPPING2_COST, TOPPING3_COST, TOPPING4_COST)

    return round(type_cost + size_cost + topping_cost, 2)

#print the order and the receipt
def print_receipt(subtotal, smoothie_type, smoothie_size, topping):
    '''
    (float, str, str, str) -> float
    
    Take in the customer's order and the subtotal. Print their order, the subtotal, the taxes and
    the final total. Return the final total.
    
    >>> print_receipt(10.99, 'Onion Toffee', 'medium', 'candy')
    You selected a medium Onion Toffee smoothie with candy.
    Smoothie cost:   10.99
    GST:     1.1
    QST:     0.55
    Total:   12.64
    12.64
        
    >>> print_receipt(103.99, 'Apple', 'galactic', 'no topping')
    You selected a galactic Apple smoothie.
    Smoothie cost:   103.99
    GST:     10.37
    QST:     5.2
    Total:   119.56
    119.56
        
    >>> print_receipt(8.69, 'Strawberry', 'small', 'coffee')
    You selected a small Strawberry smoothie with coffee.
    Smoothie cost:   8.69
    GST:     0.87
    QST:     0.43
    Total:   9.99
    9.99
    '''
    if topping == 'no topping':
        print('You selected a '+ smoothie_size + ' ' + smoothie_type + ' smoothie.')
    else:
        print('You selected a '+ smoothie_size + ' ' + smoothie_type + ' smoothie with '+ topping + '.')
        
    print('Smoothie cost:\t', subtotal)
    print('GST:\t', round(subtotal*9.975/100, 2))
    print('QST:\t', round(subtotal*5/100, 2))
    print('Total: \t', round(subtotal*114.975/100, 2))
    
    return round(subtotal*114.975/100, 2)

#place the function in order and deal with invalid choices    
def order():
    '''
    () -> NONETYPE
    
    Print welcome message, questions and options, and receipt.
    
    >>> order()    #normal situation where every choice are available and the user doesn't choose Onion Toffee
    Welcome to Smooth Smoothies Smoothie Ordering System.
    Have you tried our new Onion Toffee smoothie?
    Which smoothie do you want?
    1)  $ 3.99   Apple
    2)  $ 4.49   Banana
    3)  $ 5.69   Strawberry
    4)  $ 9.99   Onion Toffee
    Your choice (1-4): 1
    You have selected Apple.
    Unfortunately, we are out of Apple.
    You will be served Onion Toffee smoothie.
    Which size do you want?
    1)  $ -2.0   small
    2)  $ 0.0    medium
    3)  $ 2.0    large
    4)  $ 100.0      galactic
    Your choice (1-4): 1
    You have selected small.
    Which topping would you like?     #no topping neither
    1)  $ 0.0    no topping
    2)  $ 1.0    caramel
    3)  $ 1.0    coffee
    4)  $ 1.0    candy
    Your choice (1-4): 1
    You have selected no topping.
    You selected a small Onion Toffee smoothie.
    Smoothie cost:   7.99
    GST:     0.8
    QST:     0.4
    Total:   9.19
    
    >>> order()    #choice for smoothie is invalid
    Welcome to Smooth Smoothies Smoothie Ordering System.
    Have you tried our new Onion Toffee smoothie?
    Which smoothie do you want?
    1)  $ 3.99   Apple
    2)  $ 4.49   Banana
    3)  $ 5.69   Strawberry
    4)  $ 9.99   Onion Toffee
    Your choice (1-4): 5
     
    Invalid input. Please choose one of the available options.
    
    >>> order()    #choosing the onion toffee
    Welcome to Smooth Smoothies Smoothie Ordering System.
    Have you tried our new Onion Toffee smoothie?
    Which smoothie do you want?
    1)  $ 3.99   Apple
    2)  $ 4.49   Banana
    3)  $ 5.69   Strawberry
    4)  $ 9.99   Onion Toffee
    Your choice (1-4): 4
    You have selected Onion Toffee.
    Which size do you want?
    1)  $ -2.0   small
    2)  $ 0.0    medium
    3)  $ 2.0    large
    4)  $ 100.0      galactic
    Your choice (1-4): 4
    You have selected galactic.
    Which topping would you like?
    1)  $ 0.0    no topping
    2)  $ 1.0    caramel
    3)  $ 1.0    coffee
    4)  $ 1.0    candy
    Your choice (1-4): 4
    You have selected candy.
    You selected a galactic Onion Toffee smoothie with candy.
    Smoothie cost:   110.99
    GST:     11.07
    QST:     5.55
    Total:   127.61
    
    >>> order()    #Entering a string instead of an integer
    Welcome to Smooth Smoothies Smoothie Ordering System.
    Have you tried our new Onion Toffee smoothie?
    Which smoothie do you want?
    1)  $ 3.99   Apple
    2)  $ 4.49   Banana
    3)  $ 5.69   Strawberry
    4)  $ 9.99   Onion Toffee
    Your choice (1-4): 1
    You have selected Apple.
    Unfortunately, we are out of Apple.
    You will be served Onion Toffee smoothie.
    Which size do you want?
    1)  $ -2.0   small
    2)  $ 0.0    medium
    3)  $ 2.0    large
    4)  $ 100.0      galactic
    Your choice (1-4): cat
     
    Invalid input. Please choose one of the available options.
    
    >>> order()    #Invalif input for the topping choice
    Welcome to Smooth Smoothies Smoothie Ordering System.
    Have you tried our new Onion Toffee smoothie?
    Which smoothie do you want?
    1)  $ 3.99   Apple
    2)  $ 4.49   Banana
    3)  $ 5.69   Strawberry
    4)  $ 9.99   Onion Toffee
    Your choice (1-4): 2
    You have selected Banana.
    Unfortunately, we are out of Banana.
    You will be served Onion Toffee smoothie.
    Which size do you want?
    1)  $ -2.0   small
    2)  $ 0.0    medium
    3)  $ 2.0    large
    4)  $ 100.0      galactic
    Your choice (1-4): 3
    You have selected large.
    Which topping would you like?
    1)  $ 0.0    no topping
    2)  $ 1.0    caramel
    3)  $ 1.0    coffee
    4)  $ 1.0    candy
    Your choice (1-4): -7
     
    Invalid input. Please choose one of the available options.
    '''
    #welcome message
    print('Welcome to Smooth Smoothies Smoothie Ordering System.')
    print('Have you tried our new Onion Toffee smoothie?')
    
    #defining the questions
    question1 = 'Which smoothie do you want?'
    question2 = 'Which size do you want?'
    question3 = 'Which topping would you like?'
    
    #the user choose which smoothie they want
    user_type = pose_question_with_costs(question1, SMOOTHIE1_NAME, SMOOTHIE1_COST, SMOOTHIE2_NAME, SMOOTHIE2_COST, SMOOTHIE3_NAME, SMOOTHIE3_COST, SMOOTHIE4_NAME, SMOOTHIE4_COST)
    if (user_type != SMOOTHIE1_NAME and user_type != SMOOTHIE2_NAME and user_type != SMOOTHIE3_NAME and user_type != SMOOTHIE4_NAME):
        print('Invalid input. Please choose one of the available options.')
    else:
        if user_type != SMOOTHIE4_NAME:
            print('Unfortunately, we are out of ' + user_type +'.\nYou will be served Onion Toffee smoothie.')
            user_type = SMOOTHIE4_NAME
        
        #The program ask them the other questions and return their choice
        user_size = pose_question_with_costs(question2, SIZE1_NAME, SIZE1_COST, SIZE2_NAME, SIZE2_COST, SIZE3_NAME, SIZE3_COST, SIZE4_NAME, SIZE4_COST)
        if (user_size != SIZE1_NAME and user_size != SIZE2_NAME and user_size != SIZE3_NAME and user_size != SIZE4_NAME):
            print('Invalid input. Please choose one of the available options.')
        else:
            user_top = pose_question_with_costs(question3, TOPPING1_NAME, TOPPING1_COST, TOPPING2_NAME, TOPPING2_COST, TOPPING3_NAME, TOPPING3_COST, TOPPING4_NAME, TOPPING4_COST)
            if (user_top != TOPPING1_NAME and user_top != TOPPING2_NAME and user_top != TOPPING3_NAME and user_top != TOPPING4_NAME):
                print('Invalid input. Please choose one of the available options.')
            else:
                #The program calculate and print the receipt
                user_subtotal = calculate_subtotal(user_type, user_size, user_top)
                print_receipt(user_subtotal, user_type, user_size, user_top)