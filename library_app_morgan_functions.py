from book import Book
import os

def load_books(books, file_name):
    '''
    Description: Iterates over each line of the provided file, creating Book objects from each line of attributes, and appends them to the list
    Arguments: books - (list) - empty list that Book objects will be added to
                file_name - (str) - Name of CSV file with book information
    Returns: num_books - (int) - the number of books loaded
    '''
    file = open(file_name, mode = "r")
    for line in file:
        book_attributes = line.strip().split(",")
        book = Book(book_attributes[0], book_attributes[1], book_attributes[2], book_attributes[3], book_attributes[4])
        books.append(book)
    return len(books)

def print_menu(menu_heading, menu_options):
    '''
    Description: Displays menu heading and the menu options that are passed in, get input selection from user, and returns users valid selection
    Arguments: menu_heading - (str) - heading for menu
                menu_options - (dict) - includes menu options
    Returns: user_selection - (int) - valid user selection
    '''
    # print menu heading and menu options
    print(menu_heading)
    for key in menu_options:
        print(f'{key}. {menu_options.get(key)}')

    # validate user selection and return it
    valid = False
    user_selection = input("Enter your selection: ")
    if user_selection.isnumeric():
        user_selection = int(user_selection)
        if user_selection in menu_options.keys() or user_selection == 2130:
            valid = True
    while not valid:
        print("Invalid option")
        user_selection = input("Enter your selection: ")
        if user_selection.isnumeric():
            user_selection = int(user_selection)
        if user_selection in menu_options.keys():
            valid = True
    return user_selection

def search_books(books, search_string):
    '''
    Description: Iterates through list of books and checks if the search string appears in the isbn, title, author, or genre; if found, the book is added to the search result list
    Arguments: books - (list) - list of all Book objects
                search_string - (str) - string to look for within Book object attributes
    Returns: search_result - (list) - list of books that contain the search string
    '''
    search_result = []
    search_string = search_string.upper()
    for book in books:
        string_found = False
        if search_string in str(book.get_isbn()) or search_string in book.get_title().upper() or search_string in book.get_author().upper() or search_string in book.get_genre_name().upper():
            string_found = True
        if string_found:
            search_result.append(book)
    return search_result