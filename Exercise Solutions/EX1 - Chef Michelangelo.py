import math
pieces = int(input())
c = pieces * 2 - 2
delta = math.sqrt(4 * c + 1)
cuts = (-1 + delta) / 2
print(math.ceil(cuts))
