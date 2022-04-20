class NameError(Exception):
  pass

try:
  name = input('Input your name >>').strip()
  if len(name) < 1:
    raise NameError
  else:
    print("Hello,", name)
    print("Hello, stranger!")
    print("What a beautiful name you have!")
except NameError:
    print('Error')
finally:
    print("Hope to see you soon!")
