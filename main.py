class NotInBoundsError(Exception):
  def c_str_dunder(self):
    return "There is an error!"

def check_integer():
  try:
    num = int(input('Enter num from 45 of 67>>'))
    if 45 < int(num) < 67:
      print(num)
    else:
      raise NotInBoundsError
  except NotInBoundsError:
    print(NotInBoundsError)
    check_integer()

check_integer()

def error_handling():
  try:
    
