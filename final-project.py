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
            book.borrow_it()
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
            book.return_it()
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