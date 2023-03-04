input_list = [1, 2, 3, 'gg', ['a', 'b'], 'j', 'X']
target = 'gg'

index = 0
for item in input_list:
    print('item:', item)
    if item == target:
        break
    index += 1
else:
    index = -1

print('index_1:', index)
print('-' * 50)


for index, item in enumerate(input_list):
    if item == target:
        break
else:
    index = -1

print('index_2:', index)
