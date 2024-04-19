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
        book_attributes = line.strip().split(",")  # Split book attributes into list and get rid of the ending newline char
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
    # Print menu heading and menu options.
    print(menu_heading)
    for key in menu_options:
        print(f'{key}. {menu_options.get(key)}')

    # Validate user selection based on the given menu_options and return it once it is valid
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
        if user_selection in menu_options.keys() or user_selection == 2130:
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
        # If the string is found in any of the book attributes, change string_found variable to True
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
  
  # Get book information from user
  print("\n-- Add a book --")
  isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
  title = input("Enter the title: ")
  author = input("Enter author name: ")
  genre_name = input("Enter genre: ")
  
  # Loop until a valid genre name is given (case sensitive). 
  while genre_name not in Book.get_genre_names():
    print("Invalid genre. Choices are: ", end="")
    for i in range(0,len(Book.get_genre_names())-1):
        print(f'{Book.get_genre_names()[i]}, ', end="")
    print(Book.get_genre_names()[-1])
    genre_name = input("Enter genre: ")

  # Converts the genre name into its corresponding number
  genre = Book.get_genre_names().index(genre_name)
  new_book = Book(isbn,title,author,genre,"True")
  book_list.append(new_book)
  print(f"'{title}' with ISBN {isbn} successfully added.")
  
def print_books(book_list):
  '''
    Description: Receives a book list and displays book information heading and then displays each Book object on a separate line
    Arguments: book_list - (list) - list of all Book objects
    Returns: None
    '''
  print(f'{"ISBN":<14} {"Title":<25} {"Author":<25} {"Genre":<20} {"Availability":<12}')
  print("-" * 14, "-" * 25,"-" * 25,"-" * 20, "-" * 12)

  # Print each book on a separate line
  for book in book_list:
    print(book)
    
def save_books(book_list,file_name):
  '''
    Description: Receives book list and name of CSV file. Iterates over book list, formatting a comma separated string containing book attributes, writes each stringa as a separate line to the file, and then returns the number of books saved to the file
    Arguments: book_list - (list) - list of all Book objects
                file_name - (str) - name of CSV file we are writing to
    Returns: len(book_list) - (int) - number of books saved to the file
    '''
  with open(file_name,'w') as file:
    # Write each book (in csv format) to the specified file; each book is on a separate line
    for book in book_list:
        book_info = f"{book.get_isbn()},{book.get_title()},{book.get_author()},{book.get_genre()},{book.get_available()}\n"
        file.write(book_info)
  return len(book_list)



def find_book_by_isbn(isbn,bookList):
    '''
    Description: Receives a book list and an ISBN, iterates through the list of books to find the matching ISBN; if found, the index of the matching book is returned, other -1 is returned
    Arguments: isbn - (list) - list of all book objects
                bookList - (str) - ISBN to find
    Returns: index - (int) - index of matching book or -1 if no book with ISBN is found
    '''
    # Iterate through books until a matching ISBN is found; once found, return the index of the matching book
    for book in bookList:
        if isbn == book.get_isbn():
            index = bookList.index(book)
            return index
    else:
        return -1  # No match is found

def borrow_book(bookList):
    '''
    Description: Receives a book list, inputs an ISBN from the user and calls find_book_by_isbn(); if an index to a matching book was returned and that book is currently available, invokes the book’s borrow_it() method. Otherwise displays an appropriate message.
    Arguments: bookList - (list) - list of all Book objects
    Returns: None
    '''
    # Get ISBN of book to borrow
    print("\n-- Borrow a Book --")
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    index = find_book_by_isbn(isbn, bookList)
    book = bookList[index]

    # If a matching book is found, get its availability status to determine whether or not it can be borrowed, otherwise print appropriate message
    if index != -1:
        available = book.get_available()
        if available == "True":
            book.borrow_it()
            print(f"'{book.get_title()}' with ISBN {isbn} successfully borrowed.")
        else:
            print(f"'{book.get_title()}' with ISBN {isbn} is not currently available.")
    else:
        print("No book found with that ISBN.")


def return_book(bookList):
    '''
    Description: Receives a book list, inputs an ISBN from the user and calls find_book_by_isbn(); if an index to a matching book was returned and that book is currently borrowed, invokes the book’s return_it() method. Otherwise displays an appropriate message.
    Arguments: bookList - (list) - list of all Book objects
    Returns: None
    '''
    # Get ISBN of book to return
    print("\n-- Return a Book --")
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    index = find_book_by_isbn(isbn, bookList)
    book = bookList[index]

    # If a matching book is found, get its availability status to determine whether or not it can be returned, otherwise print appropriate message
    if index != -1:
        available = book.get_available()
        if available == "False":
            book.return_it()
            print(f"'{book.get_title()}' with ISBN {isbn} successfully returned.")
        else:
            print(f"'{book.get_title()}' with ISBN {isbn} is not currently borrowed.")
    else:
        print("No book found with that ISBN.")

def remove_book(bookList):
    '''
    Description: Receives a book list, inputs an ISBN from the user and calls find_book_by_isbn(); if an index to a matching book was returned, removes the book from the list. Otherwise displays an appropriate message.
    Arguments: bookList - (list) - list of all Book objects
    Returns: None
    '''
    print("\n-- Remove a book --")
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    index = find_book_by_isbn(isbn, bookList)

    # If a matching book is found, delete it from the book list, otherwise print appropriate message
    if index != -1:
        print(f"'{bookList[index].get_title()}' with ISBN {isbn} successfully removed.")
        bookList.pop(index)
    else:
        print("No book found with that ISBN.")


def main():
    print("Starting the system ...")
    file_name = input("Enter book catalog filename: ")

    # If the file does not exist, continue asking user for file name until a valid name is provided
    while not os.path.exists(file_name):
        file_name = input("File not found. Re-enter book catalog filename: ")
    print("Book catalog has been loaded.")
    book_list = []
    load_books(book_list,file_name)
    menu_heading = "\nReader's Guild Library - Main Menu\n" + "=" * 34
    menu_options = {1:"Search for books", 2:"Borrow a book", 3:"Return a book", 0:"Exit the system"}
    
    # Continue showing main menu until user enters 0 to quit the program
    user_selection = 1

    while user_selection != 0:
        user_selection = print_menu(menu_heading, menu_options)

        # If the user inputs the special password 2130, update menu_options so the user has special access on the next loop when print_menu() is called
        if user_selection == 2130:
            menu_heading = "\nReader's Guild Library - Librarian Menu\n" + "=" * 39
            menu_options = {1:"Search for books", 2:"Borrow a book", 3:"Return a book", 4:"Add a book", 5:"Remove a book", 6:"Print catalog", 0:"Exit the system"}
        
        # Call appropriate function depending on user input
        match user_selection:
            case 1:
                print("\n-- Search for books --")
                search_string = input("Enter search value: ")
                search_result = search_books(book_list, search_string)
                if len(search_result) == 0:
                    print("No matching books found.")
                else:
                    print_books(search_result)
            case 2:
                borrow_book(book_list)
            case 3:
                return_book(book_list)
            case 4:
                add_book(book_list)
            case 5:
                remove_book(book_list)
            case 6:
                print("\n-- Print book catalog --")
                print_books(book_list)
    print("\n-- Exit the system --")
    save_books(book_list, file_name)
    print("Book catalog has been saved.\nGood Bye!")

main()