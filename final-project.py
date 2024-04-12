class Book:
    GENRE_NAMES = [
"Romance",
"Mystery",                  
"Science Fiction" ,                 
"Thriller",                  
"Young Adult",                   
"Children's Fiction",              
"Self-help",                   
"Fantasy",                   
"Historical Fiction",                   
"Poetry"                   
]   
#Creat a constructor
    def __init__(self,isbn,title,author,genre,available):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__genre = int(genre)
        self.__available = bool(available)
    #Method for getting isbn
    def get_isbn(self):
        return self.__isbn
    #Method for getting title
    def get_title(self):
        return self.__title
    #Method for getting author
    def get_author(self):
        return self.__author
            
    # Method for setting the isbn
    def set_isbn(self,isbn):
        self.__isbn = isbn
    
    #Method for getting genre
    def get_genre(self):
        return self.__genre
    
    #getter method that returns the name of the genre (as a string) according to the table:
    def get_genre_name(self):
        return Book.GENRE_NAMES[self.__genre]
    
    #Method for getting available
    def get_available(self):
        return self.__available

    # additional getter method that returns a string based on the available attribute, I.e., If True Then ‘Available’ Else ‘Borrowed’.
    def get_availability(self):      
        if self.__available  is True:
            return "Available"
        else:
            return "Borrowed"
        
    # Method for setting the title
    def set_title(self,title):
        self.__title = title

    # Method for setting the author
    def set_author(self,author):
        self.__author = author

    # Method for setting the genre
    def set_genre(self,genre):
        self.__genre = genre

    #Sets the book’s available attribute to False
    def borrow_it():
        available = False

    #Sets the book’s available attribute to True
    def return_it():
        available = True
        
    #Returns a string representation of the book formatted for display. E.g.:
    def __str__(self):
        return f"{self.__isbn:<20}{self.__title:^20}{self.__author:^20}{self.get_genre_name():^20}{self.get_availability():^20}"

    '''•	Receives a book list
•	Inputs an ISBN from the user and calls find_book_by_isbn()
•	If an index to a matching book was returned and that book is currently available, invokes the book’s borrow_it() method. Otherwise displays an appropriate message.
'''
def createBookList():
    bookList = []  # Create an empty list to store book information
    with open("books.csv", mode='r') as file:
        for line in file:
            book_info = line.strip().split(',')
            bookList.append(list(book_info))  # Append each book's information as a tuple
    return bookList

bookList = createBookList()

def find_book_by_isbn(isbn,bookList):
    genre_name = ""
    for books in bookList:
        if isbn == books[0]:
            genre_name = books[3]
            return genre_name
    else:
        return '-1'

def borrow_book(bookList):
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
    isbn = input("Please enter the ISBN")
    if find_book_by_isbn(isbn,bookList) != '-1':
        for books in bookList:
            if isbn == books[0]:
                books = ""
remove_book(bookList)