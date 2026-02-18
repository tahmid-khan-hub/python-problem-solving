# Create a class called Book with attributes title and author. 
# Then create a subclass called EBook that inherits from Book and has an additional attribute called file_size_mb. 
# Implement a method in the EBook class called Details that prints out the title, author, and file size of the ebook.

class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

class EBook(Book):
  def __init__(self, title, author, file_size_mb):
    super().__init__(title, author)
    self.file_size_mb = file_size_mb
  def Details(self):
    print(f'Title: {self.title}, Author: {self.author}, Size: {self.file_size_mb}')

Book1 = EBook('The Great Gatsby', 'F. Scott Fitzgerald', 20)
Book1.Details()