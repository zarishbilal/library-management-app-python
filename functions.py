from book import Book
import os
#Add book Function
def add_book(book_list):
  print("\n-- Add a book --")
  isbn=input("Enter the ISBN:")
  title=input("Enter the title:")
  author=input("Enter the author name:")
  genre_name=input("Enter the genre name:")
  
  while genre_name not in Book.get_genre_names():
    print("Invalid genre. Choices are: ", end="")
    for i in range(0,len(Book.get_genre_names())-1):
        print(f'{Book.get_genre_names()[i]}, ', end="")
    print(Book.get_genre_names()[-1])
    genre_name = input("Enter genre: ")

  genre = Book.get_genre_names().index(genre_name)
  new_book = Book(isbn,title,author,genre,"True")
  book_list.append(new_book)
  print(f"'{title}' with ISBN {isbn} successfully added.")
  
  
  
 #Print books function 
def print_books(book_list):
    print(f'{"ISBN":<14} {"Title":<25} {"Author":<25} {"Genre":<20} {"Availability":<12}')
    print("-" * 14, "-" * 25,"-" * 25,"-" * 20, "-" * 12) 
    for book in book_list:
     print(book)
    
#Save books function
def save_books(book_list,file_name):
  file_name=input("Enter file name:")
  with open(file_name,'w') as file:
   for book in book_list:
     book_info=f"{book.get_isbn()},{book.get_title()},{book.get_author()},{book.get_genre()},{book.get_available()}\n"
     file.write(book_info)
  return len(book_list)