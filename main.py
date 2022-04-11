stock = []
for i in range(7):
  for j in range(i, 7):
    stock.append([i, j])

print(stock)
stock = [[i, j] for i in range(7) for j in range(i, 7)]