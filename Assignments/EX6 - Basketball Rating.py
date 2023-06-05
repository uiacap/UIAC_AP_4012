n = int(input())
names = input().split(",")
heights = input().split("|")
d = {}

for player_no in range(n):
    d[names[player_no]] = heights[player_no]

desired = d[input()]
rank = 1

for i in heights:
    if i > desired:
        rank += 1

print(rank)
