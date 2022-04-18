stock = [[2, 1], [2, 3]]

weights = {
  0: 7,
  1: 8
}

max_value = max(weights.values())
print(max_value)

rev_weights = {v: k for k, v in weights.items()}

max_key = stock[rev_weights[max_value]]
print(max_key)