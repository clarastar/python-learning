def append_to(element, to=[]):
  print('id', id(to))
  to.append(element)
  return to

list_1 = append_to('x')

# list_2 = append_to('y', ['a','b','c'])
# print('list_2', list_2)

# list_22 = append_to('w', ['e','f'])
# print('list_22', list_22)

list_3 = append_to('z')

print('list_1', list_1)
print('list_3', list_3)

list_4 = append_to('a')

print('list_4', list_4)

x = 10
def foo():
  global x
  x +=1
  print(x)

foo()

def foo(a, b, c, d, *args, **kwargs):
  print('args', type(args))
  print('kwargs', type(kwargs))
  print(a, b, c, d, args, kwargs)

foo(1, 2, 3, 4, 5, 11, 12, e=6, f=7, g=8)
list
