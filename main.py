# Handling Exceptions

# list
# https://docs.python.org/3/library/exceptions.html

a = 5
b = 'five'


try:
  result = a / b
except ZeroDivisionError as err:
  print('0 Error', err)
except TypeError as error:
  print('T Error', error.__class__.__name__, error)
else:
  print('The result is ', result)
finally:
  print("Thank you for using the service")


