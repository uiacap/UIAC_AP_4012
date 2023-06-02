n = int(input())
s = input().split(' ')

result_list = list(set([word for word in s if len(word) > 4 and word[0].lower() == word[-1].lower()]))
result_list.sort()

print(' '.join(result_list))
