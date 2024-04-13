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
  print("\nBook Information")
  for book in book_list:
    print(f"ISBN:{book.get_isbn()}\nTitle:{book.get_title()}\nAuthor:{book.get_author()}\nGenre Name:{book.get_genre_name()}")
    
def save_books(book_list,file_name):
  file_name = input("Enter file name:")
  with open(file_name,'w') as file:
   for book in book_list:
     book_info = f"{book.get_isbn()},{book.get_title()},{book.get_author()},{book.get_genre_name()}\n"
     file.write(book_info)
  return len(book_list)

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