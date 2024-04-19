from book import Book
import os

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
