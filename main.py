print('The outputs for A is {}. And for B is {}'.format('[11, 13, 15, 17]', '[1, 2, 3, 4, 10, 11, 12, 13]'))
list_1 = [i for i in range(0,10)]
list_2 = [i for i in range(10, 20)]

def my_product():
 res = list(map(lambda x, y: x * y ,list_1, list_2, ))
 return res
print(my_product())