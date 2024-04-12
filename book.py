class Book():
    book_table = {0:"Romance", 1:"Mystery", 2:"Science Fiction", 3:"Thriller", 4:"Young Adult", 5:"Children's Fiction", 6: "Self-help", 7: "Fantasy", 8:"Historical Fiction", 9:"Poetry"}
    def __init__(self, isbn, title, author, genre, available):
        '''Initializes all 5 attributes to the corresponding values passed in'''
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__genre = genre  # integer including 0
        self.__available = available # bool
    def get_isbn(self):
        return self.__isbn
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_genre(self):
        return self.__genre
    def get_available(self):
        # True if available, False if borrowed
        return self.__available
    def get_genre_name(self):
        '''Getter method that returns the name of the genre as a string'''
        return self.book_table.get(int(self.__genre))
    def get_availability(self):
        '''Getter method that returns string "Available" if true and 'Borrow" if false'''
        if self.get_available() == "True":
            return "Available"
        else:
            return "Borrowed"
    def set_isbn(self,isbn):
        self.__isbn = isbn
    def set_title(self,title):
        self.__title = title
    def self_author(self,author):
        self.__author = author
    def set_genre(self,genre):
        self.__genre = genre
    def borrow_it(self):
        self.__available = False
    def return_it(self):
        self.__available = True
    def __str__(self):
        '''Returns a string representation of the book formatted for display'''
        return f'{str(self.__isbn):<14} {self.__title:<25} {self.__author:<25} {self.get_genre_name():<20} {self.get_availability():<12}'

"""
book = Book(123, "Hello", "Morgan", 0,False)
print("Testing get_genre_name:",book.get_genre_name())

print("Testing get_availability:",book.get_availability())
book.set_genre(1)
print("Testing get_genre_name:",book.get_genre_name())
print(book)
I'm just practicing using GitHub commit here!
 """

#