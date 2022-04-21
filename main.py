class NegativeSumError(Exception):
  pass

def sum_with_exceptions():
  try:
    a = int(input('Enter nums:'))
    b = int(input('Enter nums:'))
    c = a + b
    if int(c) < 0:
      raise NegativeSumError
    else:
      print(c)
  except NegativeSumError:
    print('Sum negetive')
    sum_with_exceptions()
    
sum_with_exceptions()
