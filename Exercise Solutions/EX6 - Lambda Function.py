def multiply_by_num(n):
  return lambda a : a * n

x = multiply_by_num(5)
y = multiply_by_num(2)

print(f"x(3) equals {x(3)} and y(-4) equals {y(-4)}")
