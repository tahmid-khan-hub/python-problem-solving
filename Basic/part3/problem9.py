# Create a class called Book with attributes title and author. 
# Implement a method called display_info() that prints the book's title and author. Create two instances of the Book class and call the display_info() method for each instance. 
# Additionally, keep track of the total number of books created using a class variable.

class Book:
  book_count = 0
  def __init__(self, title, author):
    self.title = title
    self.author = author
    Book.book_count += 1
  def display_info(self):
    print(f'Title: {self.title}, Author: {self.author}')

Book1 = Book('The Catcher in the Rye', 'J.D. Salinger')
Book2 = Book('The Great Gatsby', 'F. Scott Fitzgerald')
Book1.display_info()
Book2.display_info()
Book.book_count