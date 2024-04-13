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

def add_book(book_list):
  '''
    Description: Receives book list, inputs ISBN, title, author, and genre name (that is then validated) from the user creates a new Book instance of appends it to the list
    Arguments: book_list - (list) - list of all book objects
    Returns: None
    '''
  isbn = input("Enter the ISBN:")
  title = input("Enter the title:")
  author = input("Enter the author name:")
  genre_name = input("Enter the genre name:")
  
  genre_id = Book.GENRE_NAME.get(genre_name)
  if genre_id is None:
    print("Invalid genre name.")
    return
  
  genre = genre_name.get(genre_id)
  new_book = Book(isbn,title,author,genre)
  book_list.append(new_book)
  print("Book added successfully")
  
def print_books(book_list):
  '''
    Description: Receives a book list and displays book information heading and then displays each Book object on a separate line
    Arguments: book_list - (list) - list of all Book objects
    Returns: None
    '''
  print("\nBook Information")
  for book in book_list:
    print(f"ISBN:{book.get_isbn()}\nTitle:{book.get_title()}\nAuthor:{book.get_author()}\nGenre Name:{book.get_genre_name()}")
    
def save_books(book_list,file_name):
  '''
    Description: Receives book list and name of CSV file. Iterates over book list, formatting a comma separated string containing book attributes, writes each stringa as a separate line to the file, and then returns the number of books saved to the file
    Arguments: book_list - (list) - list of all Book objects
                file_name - (str) - name of CSV file we are writing to
    Returns: len(book_list) - (int) - number of books saved to the file
    '''
  file_name = input("Enter file name:")
  with open(file_name,'w') as file:
   for book in book_list:
     book_info = f"{book.get_isbn()},{book.get_title()},{book.get_author()},{book.get_genre_name()}\n"
     file.write(book_info)
  return len(book_list)



def createBookList():
    '''
    Description: Receives a book list, inputs an ISBN from the user and calls find_book_by_isbn(); if an index to a matching book was returned and that book is currently available, invokes the book’s borrow_it() method. Otherwise displays an appropriate message.
    Arguments: none
    Returns: bookList - (list) - returns list of all the books
    '''
    bookList = []  # Create an empty list to store book information
    with open("books.csv", mode='r') as file:
        for line in file:
            book_info = line.strip().split(',')
            bookList.append(list(book_info))  # Append each book's information as a tuple
    return bookList


def find_book_by_isbn(isbn,bookList):
    '''
    Description: Receives a book list and an ISBN, iterates through the list of books to find the matching ISBN; if found, the index of the matching book is returned, other -1 is returned
    Arguments: isbn - (list) - list of all book objects
                bookList - (str) - ISBN to find
    Returns: index - (int) - index of matching book or -1 if no book with ISBN is found
    '''
    genre_name = ""
    for books in bookList:
        if isbn == books[0]:
            genre_name = books[3]
            return genre_name
    else:
        return '-1'

def borrow_book(bookList):
    '''
    Description: Receives a book list, inputs an ISBN from the user and calls find_book_by_isbn(); if an index to a matching book was returned and that book is currently available, invokes the book’s borrow_it() method. Otherwise displays an appropriate message.
    Arguments: bookList - (list) - list of all Book objects
    Returns: None
    '''
    isbn = input("Please enter the ISBN")
    if find_book_by_isbn(isbn,bookList) != '-1':
        for books in bookList:
            if isbn == books[0]:
                available = books[4]
        if available == 'True':
            Book.borrow_it()
            print("borrow_it applied")
        else:
            print("Book isCurrently unavailable")
    else:
        print("PLease enter correct isbn")


def return_book(bookList):
    '''
    Description: Receives a book list, inputs an ISBN from the user and calls find_book_by_isbn(); if an index to a matching book was returned and that book is currently borrowed, invokes the book’s return_it() method. Otherwise displays an appropriate message.
    Arguments: bookList - (list) - list of all Book objects
    Returns: None
    '''
    isbn = input("Please enter the ISBN")
    if find_book_by_isbn(isbn,bookList) != '-1':
        for books in bookList:
            if isbn == books[0]:
                available = books[4]
        if available == 'False':
            Book.return_it()
            print("return_it applied")
        else:
            print("Book isCurrently unavailable")
    else:
        print("PLease enter correct isbn")

def remove_book(bookList):
    '''
    Description: Receives a book list, inputs an ISBN from the user and calls find_book_by_isbn(); if an index to a matching book was returned, removes the book from the list. Otherwise displays an appropriate message.
    Arguments: bookList - (list) - list of all Book objects
    Returns: None
    '''
    isbn = input("Please enter the ISBN")
    if find_book_by_isbn(isbn,bookList) != '-1':
        for books in bookList:
            if isbn == books[0]:
                books = ""
    remove_book(bookList)


def main():
    print("Starting the system ...")
    file_name = input("Enter book catalog filename: ")
    while not os.path.exists(file_name):
        file_name = input("File not found. Re-enter book catalog filename: ")
    print("Book catalog has been loaded.")
    book_list = []
    load_books(book_list,file_name)
    menu_heading = "\nReader's Guild Library - Main Menu\n" + "=" * 34
    menu_options = {1:"Search for books", 2:"Borrow a book", 3:"Return a book", 0:"Exit the system"}
    
    # continue showing main menu until user enters 0
    user_selection = 1

    while user_selection != 0:
        user_selection = print_menu(menu_heading, menu_options)
        if user_selection == 2130:
            menu_heading = "\nReader's Guild Library - Librarian Menu\n" + "=" * 39
            menu_options = {1:"Search for books", 2:"Borrow a book", 3:"Return a book", 4:"Add a book", 5:"Remove a book", 6:"Print catalog", 0:"Exit the system"}
        match user_selection:
            case 1:
                print("\n-- Search for books --")
                search_string = input("Enter search value: ")
                search_result = search_books(book_list, search_string)
                if len(search_result) == 0:
                    print("No matching books found.")
                else:
                    # print_books(search_result)
                    pass
            
    print("-- Exit the system --")
    # save_books(book_list, file_name)
    print("Book catalog has been saved.\nGood Bye!")

main()