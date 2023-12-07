#Author: Christine Yang-Dai
#This program assists in the shipment of books in a depot.

#function for calculating the checksum
def calculate_isbn_checksum_by_digits(d1, d2, d3, d4, d5, d6, d7, d8, d9):
    '''
    (int, int, int, int, int, int, int, int, int) -> str
    
    The function takes in 9 integers representing the first 9 digits of the isbn.
    Return the checksum as a string
    
    >>> calculate_isbn_checksum_by_digits(1, 2, 3, 4, 5, 6, 7, 8, 9)
    'X'
    
    >>> calculate_isbn_checksum_by_digits(1, 1, 1, 1, 1, 1, 1, 1, 1)
    '1'
    
    >>> calculate_isbn_checksum_by_digits(8, 7, 1, 1, 0, 7, 5, 5, 9)
    '7'
    
    >>>calculate_isbn_checksum_by_digits(0, 0, 0, 0, 0, 0, 0, 0, 0)
    '0'
    '''
    checksum_by_digits = (d1+2*d2+3*d3+4*d4+5*d5+6*d6+7*d7+8*d8+9*d9) % 11
    
    if checksum_by_digits >= 10:
        checksum_by_digits = 'X'
    else:
        checksum_by_digits = str(checksum_by_digits)
    
    return checksum_by_digits

#transforming a string of isbn to integer and calculating the checksum
def calculate_isbn_checksum(isbn):
    '''
    (int) -> str or NoneType
    
    Take in an integer representing the first 9 digits of the isbn.
    Return the checksum as a string.
    
    >>> calculate_isbn_checksum(123456789)
    'X'
    
    >>>calculate_isbn_checksum(111111111)
    '1'
    
    >>>calculate_isbn_checksum(871107559)
    '7'
    
    >>> calculate_isbn_checksum(1234567890)
    Invalid input
    '''
    if isbn < 1000000000:
        x1 = isbn // 10**8
        x2 = (isbn % 10**8) // 10**7
        x3 = (isbn % 10**7) // 10**6
        x4 = (isbn % 10**6) // 10**5
        x5 = (isbn % 10**5) // 10**4
        x6 = (isbn % 10**4) // 10**3
        x7 = (isbn % 10**3) // 10**2
        x8 = (isbn % 10**2) // 10**1
        x9 = isbn % 10**1
        
        isbn_checksum = calculate_isbn_checksum_by_digits(x1, x2, x3, x4, x5, x6, x7, x8, x9)
        return isbn_checksum
    else:
        print("Invalid input")

#This function check if the entered isbn calculated to the same checksum as the entered checksum
def is_isbn(isbn, checksum):
    '''
    (int, str) -> bool
    
    Take in an integer representing the first 9 digits of the isbn and the checksum as a string.
    Compare the checksum calculated from the isbn and the given checksum.
    Return the boolean value.
    
    >>>is_isbn(123456789, 'X')
    True
    
    >>>is_isbn(123456789, '10')
    False
    
    >>>is_isbn(871107559, "4")
    False
    
    >>> is_isbn(871107559, "7")
    True
    
    >>> is_isbn(871107559, "7")
    Invalid input
    False
    '''
    return bool(calculate_isbn_checksum(isbn) == checksum)

#This function check if the given book fit in the given box.
def book_fits_in_box(box_w, box_d, box_h, book_w, book_d, book_h):
    '''
    (int, int, int, int, int, int) -> bool or NoneType
    
    Returns True if the book of the given integer dimensions can fit in the box of the
    given integer dimensions, and False otherwise.
    
    >>> book_fits_in_box(20, 10, 5, 8, 6, 4)
    True
    
    >>> book_fits_in_box(10, 5, 20, 8, 6, 4)
    True
    
    >>> book_fits_in_box(5, 20, 10, 8, 6, 4)
    True
    
    >>> book_fits_in_box(20, 5, 10, 8, 6, 4)
    True
    
    >>> book_fits_in_box(5, 10, 20, 8, 6, 4)
    True
    
    >>> book_fits_in_box(10, 20, 5, 8, 6, 4)
    True
    
    >>> book_fits_in_box(8, 6, 4, 20, 10, 5)
    False
    
    >>> book_fits_in_box(8, 6, 4, 10, 5, 20)
    False
    
    >>> book_fits_in_box(8, 6, 4, 5, 20, 10)
    False
    
    >>> book_fits_in_box(8, 6, 4, 20, 5, 10)
    False
    
    >>> book_fits_in_box(8, 6, 4, 5, 10, 20)
    False
    
    >>> book_fits_in_box(8, 6, 4, 10, 20, 5)
    False
    
    >>> book_fits_in_box(10, 10, 10, 10, 10, 10)
    True
    
    >>> book_fits_in_box(8, 5, 5, 8, 6, 4)
    False
    
    >>> book_fits_in_box(-8, 5, 5, 8, 6, 4)
    Invalid input
    '''
    if (box_w > 0) and (box_d > 0) and (box_h > 0) and (book_w > 0) and (book_d > 0) and (book_h > 0):
        no_rotation = bool(book_w <= box_w and book_d <= box_d and book_h <= box_h)
        xyz_rotation = bool(book_h <= box_w and book_w <= box_d and book_d <= box_h)
        zyx_rotation = bool(book_d <= box_w and book_h <= box_d and book_w <= box_h)
        xy_rotation = bool(book_d <= box_w and book_w <= box_d and book_h <= box_h)
        yz_rotation = bool(book_w <= box_w and book_h <= box_d and book_d <= box_h)
        xz_rotation = bool(book_h <= box_w and book_d <= box_d and book_w <= box_h)
    
        return bool(no_rotation or xyz_rotation or zyx_rotation or xy_rotation or yz_rotation or xz_rotation)
    else:
        print("Invalid input")

#This function finds the smallest box in which the given book fits.
def get_smallest_box_for_book(book_w, book_d, book_h):
    '''
    (int, int, int) -> str
    
    Take in the dimensions of the book as an integer.
    Return the smallest box in which it would fit.
    
    >>> get_smallest_box_for_book(15, 15, 3)
    'medium'
    
    >>> get_smallest_box_for_book(15, 16, 3)
    'large'
    
    >>> get_smallest_box_for_book(8, 2, 7)
    'small'
    
    >>> get_smallest_box_for_book(100, 100, 100)
    'none can contain the book.'    
    '''
    if book_fits_in_box(10, 10, 2, book_w, book_d, book_h):
        return "small"
    elif book_fits_in_box(15, 15, 3, book_w, book_d, book_h):
        return "medium"
    elif book_fits_in_box(20, 20, 4, book_w, book_d, book_h):
        return "large"
    else:
        return "none can contain the book."

#This function calculates how many books fit in the box
def get_num_books_for_box(box_w, box_d, box_h, book_w, book_d, book_h):
    '''
    (int, int, int, int, int, int) -> int or str
    
    Take in the dimensions of the books and the box as an integer.
    Return the number of books that can fit in the box as an integer.
    
    >>>get_num_books_for_box(20, 20, 4, 7, 5, 2)
    16
    
    >>>get_num_books_for_box(10, 10, 2, 8, 2, 7)
    0
    
    >>>get_num_books_for_box(15, 15, 3, 14, 5, 1)
    9
    
    >>> get_num_books_for_box(-15, 15, 3, 14, 5, 1)
    'Invalid input'
    '''
    if (box_w > 0) and (box_d > 0) and (box_h > 0) and (book_w > 0) and (book_d > 0) and (book_h > 0): 
        w = box_w // book_w
        d = box_d // book_d
        h = box_h // book_h
        return w*d*h
    else:
        return "Invalid input"

#Run the main code for the execution of the program to aid in the shipment of books.
def main():
    '''
    () -> NoneType
    
    Print welcome message and options. Prompt user to enter an option
    and run the appropriate function.
    
    >>> main()
    Welcome to the shipment calculation system.
    1) Check ISBN
    2) Check box/book size
    3) Get smallest box size for book
    4) Get num equally-sized books per box
    Enter choice(1-4): 1
    Enter ISBN: 123456789
    Enter checksum: X
    ISBN is valid (checksum matched).
    
    >>> main()
    Welcome to the shipment calculation system.
    1) Check ISBN
    2) Check box/book size
    3) Get smallest box size for book
    4) Get num equally-sized books per box
    Enter choice(1-4): 2
    Enter the width of the book in cm: 8
    Enter the depth of the book in cm: 3
    Enter the height of the book in cm: 10
    Enter the size of the box (small, medium, large): small
    Package does not fit in box.
    
    >>> main()
    Welcome to the shipment calculation system.
    1) Check ISBN
    2) Check box/book size
    3) Get smallest box size for book
    4) Get num equally-sized books per box
    Enter choice(1-4): 3
    Enter the width of the book in cm: 8
    Enter the depth of the book in cm: 3
    Enter the height of the book in cm: 10
    The dimension of the box that fit the book is : medium
    
    >>> main()
    Welcome to the shipment calculation system.
    1) Check ISBN
    2) Check box/book size
    3) Get smallest box size for book
    4) Get num equally-sized books per box
    Enter choice(1-4): 4
    Enter the width of the book in cm: 10
    Enter the depth of the book in cm: 8
    Enter the height of the book in cm: 3
    Enter the size of the box (small, medium, large): large
    4 book(s) fit in the box
    
    >>> main()
    Welcome to the shipment calculation system.
    1) Check ISBN
    2) Check box/book size
    3) Get smallest box size for book
    4) Get num equally-sized books per box
    Enter choice(1-4): 1
    Enter ISBN: 1234556789
    Enter checksum: W
    Invalid input
    ISBN is not valid (checksum did not match)

    >>> main()
    Welcome to the shipment calculation system.
    1) Check ISBN
    2) Check box/book size
    3) Get smallest box size for book
    4) Get num equally-sized books per box
    Enter choice(1-4): 2
    Enter the width of the book in cm: -1
    Enter the depth of the book in cm: 2
    Enter the height of the book in cm: 3
    Enter the size of the box (small, medium, large): small
    Invalid input
    Package does not fit in box.

    >>> main()
    Welcome to the shipment calculation system.
    1) Check ISBN
    2) Check box/book size
    3) Get smallest box size for book
    4) Get num equally-sized books per box
    Enter choice(1-4): cat
    Invalid input

    >>> main()
    Welcome to the shipment calculation system.
    1) Check ISBN
    2) Check box/book size
    3) Get smallest box size for book
    4) Get num equally-sized books per box
    Enter choice(1-4): 3
    Enter the width of the book in cm: -6
    Enter the depth of the book in cm: 10000
    Enter the height of the book in cm: 2
    Invalid input

    >>> main()
    Welcome to the shipment calculation system.
    1) Check ISBN
    2) Check box/book size
    3) Get smallest box size for book
    4) Get num equally-sized books per box
    Enter choice(1-4): 4
    Enter the width of the book in cm: -3
    Enter the depth of the book in cm: -2
    Enter the height of the book in cm: -7
    Invalid input
    '''
    print ("Welcome to the shipment calculation system.")
    print("1) Check ISBN")
    print("2) Check box/book size")
    print("3) Get smallest box size for book")
    print("4) Get num equally-sized books per box")
    choice = input("Enter choice(1-4): ")
    
    if choice == '1':
        user_isbn = int(input("Enter ISBN: "))
        user_checksum = input("Enter checksum: ")
        if is_isbn(user_isbn, user_checksum):
            print("ISBN is valid (checksum matched).")
        else:
            print("ISBN is not valid (checksum did not match)")
    elif choice == '2':
        book_w = int(input("Enter the width of the book in cm: "))
        book_d = int(input("Enter the depth of the book in cm: "))
        book_h = int(input("Enter the height of the book in cm: "))
        
        box_size = input("Enter the size of the box (small, medium, large): ")
        if box_size == 'small':
            box_w = 10
            box_d = 10
            box_h = 2
        elif box_size == 'medium':
            box_w = 15
            box_d = 15
            box_h = 3
        elif box_size == 'large':
            box_w = 20
            box_d = 20
            box_h = 4
        else:
            print("Invalid size")
        
        if book_fits_in_box(box_w, box_d, box_h, book_w, book_d, book_h):
            print("Package fit in box.")
        else:
            print("Package does not fit in box.")
    elif choice == '3':
        book_w = int(input("Enter the width of the book in cm: "))
        book_d = int(input("Enter the depth of the book in cm: "))
        book_h = int(input("Enter the height of the book in cm: "))
        
        if (book_w or book_d or book_h) <= 0:
            print("Invalid input")
        else:
            print("The dimension of the box that fit the book is :", get_smallest_box_for_book(book_w, book_d, book_h))
    elif choice == '4':
        book_w = int(input("Enter the width of the book in cm: "))
        book_d = int(input("Enter the depth of the book in cm: "))
        book_h = int(input("Enter the height of the book in cm: "))
        
        if (book_w or book_d or book_h) <= 0:
            print("Invalid input")
        else:
            box_size = input("Enter the size of the box (small, medium, large): ")
            if box_size == 'small':
                box_w = 10
                box_d = 10
                box_h = 2
                
                print(get_num_books_for_box(box_w, box_d, box_h, book_w, book_d, book_h), "book(s) fit in the box")
            elif box_size == 'medium':
                box_w = 15
                box_d = 15
                box_h = 3
                
                print(get_num_books_for_box(box_w, box_d, box_h, book_w, book_d, book_h), "book(s) fit in the box")
            elif box_size == 'large':
                box_w = 20
                box_d = 20
                box_h = 4
                
                print(get_num_books_for_box(box_w, box_d, box_h, book_w, book_d, book_h), "book(s) fit in the box")
            else:
                print("Invalid size")

    else:
        print("Invalid input")