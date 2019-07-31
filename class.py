# class
# 1. the class keyword
# 2. the self keyword
# 3. the __init__ method
# 4. the class attributes
# 5. the instance attributes

# the class keyword
class Bookstore:
  pass

# that is self? 
class Bookstore:
  instances = 0
  def __init__(self, attrib1, attrib2):
    print('__init__ constructor gets called')
    self.attrib1 = attrib1
    self.attrib2 = attrib2
    Bookstore.instances +=1

b1 = Bookstore("", "")
b2 = Bookstore("", "")
# print('Bookstore instances', Bookstore.instances)

# An example
class BookstoreC: 
  noOfBooks = 0
  def __init__(self, title, author):
    self.title = title
    self.author = author
    BookstoreC.noOfBooks += 1

  def BookInfo(self):
    print('Book title:', self.title)
    print('Book author:', self.author)

# Create a virtual book store 
b1 = BookstoreC('Great Expectations', 'Charles Dickens')
b2 = BookstoreC('War and Peace', 'Leo Tolstoy')
b3 = BookstoreC('MiddleMarch', 'George Eliot')

b1.BookInfo()
b2.BookInfo()
b3.BookInfo()
print('Bookstore no of books', BookstoreC.noOfBooks)