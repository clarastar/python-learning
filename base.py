# numbers
# the number types are automatically upcast in the following order
Int -> Long -> Float -> complex
# test the type of numbers in python 
isinstance(2, int)
# the complex type
x = 3 + 4j 
x.real => 3
x.imag => 4.0

# Binany  二进制  begins with 0b
0b101
# Octal 八进制 begins with 0o
0o123
# Hex  十六进制  begins with 0x
0x123

# Two ways to do type conversion in python 
# basic operations
2 + 4.5 =>6.5
# built-in functions 
int(3.5)
float(3)
complex(4+7j)

# modules related to number
# decimal 
import decimal
decimal.Decimal(2.5)
# fractions
import fractions 
fractions.Fraction(2.5)

# built-in functions
round(33.5)
max(1,2,3)
min(2, 3, 4)
sqrt(4)



# Set 
# Create a set of numbers
py_set_num = {3, 7, 11}
print(py_set_num)
# Create a set of mixed data types
py_set_num = {1, '2', {1, 2}}
# set can't store duplicate elements
# it will automatically filter the duplicates

# Create a set using the set() method
py_set_mix = set(11, '1', {2, 3})

# Create set with dynamic elements
py_list = [11, 1.1, "11", (1, 2)]
py_list.append(12)

# Modify set in Python
# add an element to a set 
py_set_num.add(99) 
# delete an element from a set
py_set_num.discard(99)
py_set_num.discard(100) => OK
py_set_num.remove(100) => KeyError
# delete an unknown element
py_set_num.pop()
# clear all elements from the set
py_set_num.clear()

# Native Operations
# union operation: two ways
setA = {'a', 'b', 'c'}
setB = {'c', 'd', 'e', 'f'}
setA | setB = setA.union(setB)
# intersection operation: two ways
setA & setB = setA.intersection(setB) = setB.intersection(setA)
# difference opration
diffAB = setA - setB   # 等价于  setA.difference(setB)
diffBA = setB - setA  # 等价于  setB.difference(setA)
# symmetric diff
symdiffAB = setA^setB == setB^setA

# Miscellaneous operations
basket = set(['apple', 'banana', 'orange', 'grape'])
for fruit in basket:
  print(fruit)

#frozen set
basket = frozenset(['apple', 'orange', 'grape'])



# tuple
# Create an empty tuple
empty_tuple = () 

# Create a tuple without using a branket
py_tuple = 2, 3, 4

# Create a tuple of numbers
py_tuple = (2, 3, 4)

# Create a tuple of mixed numbers
py_tuple = (33, 3.3, 3+3j)

#Create a tuple of mixed data types
py_tuple = (33, 'a', [2])

# Create a tuple of tuples
py_tuple = ((2,3), ('q'))

## Feature1: nested
first_tuple = (1, 2, 3)
second_tuple = (a, b, c)
nested_tuple = (first_tuple, second_tuple)
print(nested_tuple)

## Feature2: multiplied
sample_tuple = ('python 1')
sample_tuple = sample_tuple*3
#####? sample_tuple 会变成字符串类型的
print(sample_tuple)


# Dictionary
# Define a blank dictionary with dictionary
blank_dict = {}

# Define a dictionary with numeric keys
num_dict = {1: 'apple', 2: 'banana'}

# Define a dictionary with keys having different types
misc_dict = {'class': 'animal', 1: [2, 3, 4, 5]}

# Create a dict with dict() method
get_dict_from_func = dict({1: 'water', 2: 'melon'})

# Create a dict from a sequence of tuples
make_dict_from_seq = dict([(1, 'melon'), (2, 'orange')])

# Access Elements
hobby_dict = {'lemon': 'fruit', 'beer': 'wine'}
print('fruit', hobby_dict['leomon'])

# Append element: two ways
hobby_dict['literature'] = 'poem'
hobby_dict.update({'literature': 'poem'})

# Update an Element
hobby_dict['lemon'] = 'acid'
hobby_dict.update(lemon='acid')

# Remove Elements
# Delete a specific element
weekdays = {1: 'Monday', 2:'Tuesday', 3: 'Wensday', 4: 'Thursday', 5: 'Friday'}
weekdays.pop(1)

# Remove a specific element: two ways
del weekdays[1]

# What is the difference between weekdays.pop(1) and del weekdays[1]

# Delete a random element
weekdays.popitem()

# Delete all elements from the dictionary
weekdays.clear()

# Eliminate the whole dictionaary
del weekdays

# Dictionary Attributes
# Dictionary Attributes1: the same key can't have another value in the dictionary
# Dictionary Attributes2: the dictionary keys should derive from the immutable data types

#Iterate Dictionary
weekdays = {1: 'Monday', 2:'Tuesday', 3: 'Wensday', 4: 'Thursday', 5: 'Friday'}
for key in weekdays:
  print('key', key)

for key, value in weekdays.items():
  print(key,":", value)


#Lists
hobbies = ['reading', 'playing', 'eating']

#Lists can be indexed and sliced
# return the first element in Lists
hobbies[0]
#return the first two elements in Lists
hobbies[:2]
# return the last element in Lists
hobbies[-1] 
#return the last three elements in Lists
hobbies[-3:] 
#return a new copy of the List
hobbies[:]
#support operation like concatination
hobbies + ['chopping']
#immute one item
hobbies[2]='singing'
#immute several items
hobbies[1:3] =['shopping', 'botany']
hobbies[1:3]=[]
#add new items at the end of the list by using append()
hobbies.append('exercing')

#built-in method len
len(hobbies)

# nest lists
courses = ['coding', 'methmatics']
life = [hobbies, courses]
life[0][0]

# Built-in python operators
# Arithmetic Operators
a = 2
b = 4
print('Sum:', a + b)
print('Subtraction:', a - b)
print('Multiplication:', a * b)
print('Division(float):', a/b)
print('Division(floor):', a//b)
print('Modulus:', a%b)
print('Exponent:', a**b)

# Comparison Operators

# Logical Operators
a = 2 
b = 3 
a and b 
a or b 
not a 

# Bitwise Operators
a >> b
a ^ b
 
# Assignment Operators 
a+ = 4
a- = 4
a* = 4
