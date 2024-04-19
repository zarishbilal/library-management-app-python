class Book:
  def __init__(self,isbn,title,author,genre,available):
    self.__isbn =isbn
    self.__title=title
    self.__author=author
    self.__genre=int(genre)
    self.__available=bool(available)
  
  def get_isbn(self):
    return self.__isbn
  
  def set_name(self,isbn):
    self.__isbn=isbn
    
  def get_title(self):
    return self.__title
  
  def set_title(self,title):
    self.__title=title
    
  def get_author(self):
    return self.__author
  
  def set_author(self,author):
    self.__author=author
  
  def get_genre(self):
    return self.__genre
  
  def set_genre(self,genre):
    self.__genre=genre
  
  def get_available(self):
    return self.__available
  
  def set_available(self,available):
    self.__available=available
  
  def get_availability(self):
    return "Available" if self.__available else "Borrowed"
  
  def borrow_it(self):
    self.__available=False
    
  def return_it(self):
    self.__available=True
    
  
    
  GENRE_NAMES={
  0:"Romance",
  1:"Mystery",
  2:"Science Fiction",
  3:"Thriller",
  4:"Young Adult",
  5:"Children's Fiction",
  6:"Self-help",
  7:"Fantasy",
  8:"Historical Fiction",
  9:"Poetry"
  }
  
  def __init__(self,genreID):
    self.__genre_id=genreID
    
  def get_genre(self):
    return self.GENRE_NAMES.get(self.genre_id,"Unknown")
  
#dummy 
genre = Genre(2)
print("Genre Name:", genre.get_genre_name()) 

def __str__(self):
  return f"{self.__isbn:<20}{self.__title:^20}{self.__author:^20}{self.get_genre():^20}{self.get_availability():^20}"

for_instance=Book("567891234569", "hen", "alwrence anna ", 5, True)
print(for_instance)
