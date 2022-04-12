income = int(input())

if 0 <= income < 15000:
  income = income = int(input(40000))

if 15000 <= income < 40000:
  income = income * 0.15

if 40000 <= income < 130000:
  income = income * 0.25

if 130000 <= income:
  income = income * 0.28

print(income)
