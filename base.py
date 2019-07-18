
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

# Update a Element
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