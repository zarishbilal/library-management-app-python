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

class book:
    def __init__(self,isbn,title,author,genre,available):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__genre = int(genre)
        self.__available = bool(available)
    #Method for getting isbn
    def getisbn(self):
        return self.__isbn
    
    # Method for setting the isbn
    def setisbn(self,isbn):
        self.__isbn = isbn
    
    #Method for getting title
    def gettitle(self):
        return self.__title
    
    # Method for setting the title
    def settitle(self,title):
        self.__title = title

    #Method for getting author
    def getauthor(self):
        return self.__author
    
    # Method for setting the author
    def setauthor(self,author):
        self.__author = author

    #Method for getting genre
    def getgenre(self):
        return self.__genre
    
    # Method for setting the genre
    def setgenre(self,genre):
        self.__genre = genre

    #getter method that returns the name of the genre (as a string) according to the table:
    def get_genre_name(self):
        return GENRE_NAMES[self.__genre]

    #Method for getting available
    def getavailable(self):
        return self.__available
    
    # Madditional getter method that returns a string based on the available attribute, I.e., If True Then ‘Available’ Else ‘Borrowed’.
    def get_availability(self):      
        if self.__available  is True:
            return "Available"
        else:
            return "Borrowed"

    #Sets the book’s available attribute to False
    def borrow_it():
        available = False

    #Sets the book’s available attribute to True
    def return_it():
        available = True
        
    #Returns a string representation of the book formatted for display. E.g.:
    def __str__(self):
        return f"{self.__isbn:<20}{self.__title:^20}{self.__author:^20}{self.get_genre_name():^20}{self.get_availability():^20}"