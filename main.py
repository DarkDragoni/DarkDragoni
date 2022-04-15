# 4 task 03
from random import randint


names = ['Денис', 'Дима1', 'Ваня', 'Дима2', 'Дима3', 'Лёша', 'Вова', 'Вадим', 'Богда', 'Юра', 'Антон', 'Артём', 'Костя']
names.sort()

math = [randint(25, 50) for _ in range(len(names))]
eng = [randint(25,50) for _ in range(len(names))]
phys = [randint(25,50) for _ in range(len(names))]

res = list(map(lambda x, y, z: x + y + z, math, eng, phys))

enroll = []

for names, point in zip(names, res):
  if point > 100:
    enroll.append([names, point])

print(enroll)
