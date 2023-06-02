n = int(input())
non_reversed_set = set()
for i in range(n):
    nums = list(map(float, input().split()))
    for i in range(len(nums)):
        this_num = nums[i]
        this_num = round(this_num, 1)
        if this_num % 1 == 0:
            this_num = int(this_num)
        non_reversed_set.add(this_num)

reversed_set = sorted(non_reversed_set, reverse=True)

for num in reversed_set:
    print(num, end=' ')
