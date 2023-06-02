n, b = map(int, input().split())
converted = ""

while n:
    converted = converted + str(n % b)
    n //= b

print(m.count("1"))
