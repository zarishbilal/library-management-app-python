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
    #Create a constructor
    def __init__(self,isbn,title,author,genre,available):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__genre = int(genre)
        self.__available = available

    #Method for getting isbn
    def get_isbn(self):
        return self.__isbn
    
    #Method for getting title
    def get_title(self):
        return self.__title
    
    #Method for getting author
    def get_author(self):
        return self.__author
    
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
        if self.__available == "True":
            return "Available"
        else:
            return "Borrowed"
        
    # Method for setting the isbn
    def set_isbn(self,isbn):
        self.__isbn = isbn
        
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
    def borrow_it(self):
        self.__available = "False"

    #Sets the book’s available attribute to True
    def return_it(self):
        self.__available = "True"
        
    #Returns a string representation of the book formatted for display. E.g.:
    def __str__(self):
        return f'{str(self.__isbn):<14} {self.__title:<25} {self.__author:<25} {self.get_genre_name():<20} {self.get_availability():<12}'
