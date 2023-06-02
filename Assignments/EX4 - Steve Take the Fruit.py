n = int(input())
file_path_dict = {}

any_to_delete = False

for i in range(n):
    file_path = input()
    file_name = file_path.split('/')[-1]

    if not len(file_path_dict.get(file_name, set())):
        file_path_dict[file_name] = set()
    file_path_dict[file_name].add(file_path)
    if len(file_path_dict[file_name]) > 1:
        any_to_delete = True


file_path_dict = dict(sorted(file_path_dict.items()))

if any_to_delete:
    for file_name, file_path_set in file_path_dict.items():
        if len(file_path_set) > 1:
            print(f'{len(file_path_set) - 1} {file_name}')
else:
    print(0)
