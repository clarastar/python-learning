def fn1():
  global x
  x = [1, 2]; y = [2, 200]
  
fn1()
try:
  print(x, y)
except Exception as ex:
  print('y->', ex)
  print('x->', x)
  # print('y->', y)

