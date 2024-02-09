old_dict = {'aa': 1, 'b': 2, 'cccc': 3, 'ddd': 'red'}

for key, value in old_dict.items():
    print(f'key: {key}, value: {value}')


for item in old_dict.items():
    print(f'item: {item}')


my_list = [[1, 2, 3], [5, 6, 7], [8, 9], [11, 12, 13, 14]]
for x, y, *z in my_list:
    print(f'x: {x}, y: {y}, z: {z}')
