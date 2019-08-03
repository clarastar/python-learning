def openFile():
  file = open("email.txt", 'w')
  file.write('clarastar')
  file.close()

openFile()

def handle():
  with open("email.txt") as fp:
    print('fp', fp.readline())
    return fp.read()

handle()

