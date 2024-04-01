my_list = [1, 0, 56, 2, 34, 10, 2]

target = 10

for index, item in enumerate(my_list):
    if item == target:
        break
else:
    index = -1

print('index:', index)
