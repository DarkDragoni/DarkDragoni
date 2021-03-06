# Binary Search

from random import randint as rr
from linear import linear
from binary import binary


n = 10_000
array = [n for n in range(n + 1)]


def rotate(array):
  for _ in range(rr(1, len(array))):
    # array.append(array.pop(0))
    array.insert(0, array.pop())
  return array

array = rotate(array)


print(linear(array))
print(binary(array, 0, len(array) - 1))
