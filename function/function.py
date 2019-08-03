# How to create a function
# single line function
def single_line(): statement
# python function with docstring
def fn(arg1, arg2):
  """docstring"""
  pass
  statement1
  statement2
# nested python function
def fn(arg1, arg2):
  """docstring"""
  pass
  statement1
  statement2
  def fn_new(arg1, arg2):
    pass
    statement1
    statement2

# Example of a function call
def typeOfNum(num):
  if num % 2 == 0:
    def message():
      print('You entered an even number')
  else:
    def message():
      print('You entered an odd number')
  message()

typeOfNum(5)
typeOfNum(6)

# Polymorphism in python
def product(x, y):return x*y
print(product(4, 9))
print(product('Python!', 2))
#print(product('python', 'exercise')) # typeError

# Parameters in a function
# Parameters are the variables used in the function definition whereas arguments are the values we pass to the function parameters
def test1(a, b):
  a = 'George'
  b[0] = 'Python'
def test2(a, b):
  a = 'George 2'
  b = [4, 5, 6]
  b[0] = 'Python3'

arg1 = 10
arg2 = [1, 2, 3, 4]
test1(arg1, arg2)
print('after executing test1:', arg1, arg2)
test2(arg1, arg2)
print('after executing test2:', arg1, arg2)
# how to avoid changing the mutable argument
test1(arg1, arg2[:])

# arguments
# standard arguments
def fn(value):
  print(value)
  return
fn(6666)  # err
# keyword-based arguments
def fn(value):
  print(value)
  return
fn(value='light')
# arguments with default values
def daysInYear(is_leap_year=False):
  if not is_leap_year:
    print('365 days')
  else:
    print('366 days')
  return
daysInYear()
daysInYear(True)

# arguments
def inventory(category, * items):
  print("%s [items=%d]:" % (category, len(items)), items)
  for item in items:
    print("-", item)
  return
inventory('Electronics', 'tv', 'lcd', 'ac', 'refrigerator', 'heater')

# Function attributes
def testFunc():
  print('I am just a test function')

testFunc.attr1 = 'Hello'
testFunc.attr2 = 'World'
testFunc ()

print(dir(testFunc))

# Python functions as objects
def testFunc(a, b): print('testFunc is called')
fn = testFunc
fn(22, 'bb')

