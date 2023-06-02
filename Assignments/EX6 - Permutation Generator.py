def permutations(lst):
    if len(lst) == 0:
        yield []
    elif len(lst) == 1:
        yield lst
    else:
        for i in range(len(lst)):
            rest = lst[:i] + lst[i+1:]
            for permutation in permutations(rest):
                yield [lst[i]] + permutation

my_list = input().split()
my_list = list(map(int,my_list))
for perm in permutations(my_list):
    print(perm)
