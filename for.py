# for loop clause
for iter in range(0, 3):
  print("iter: % d" %(iter))

# Range() Function With For Loop
books = ['C', 'C++', 'Java', 'Python']
for index in range(len(books)):
   print('Book (%d):' % index, books[index])

# for-else clause with python for loop
birds = ['Belle', 'Coco', 'Juniper', 'Lilly', 'Snow']
ignoreElse = False

for theBird in birds:
    print(theBird )
    if ignoreElse and theBird is 'Snow':
        break
else:
    print("No birds left.")