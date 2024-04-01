# print('Hello'.find('w'))

my_list = [1, 0, 56, 2]

target = 101

index = 0
while index < len(my_list):
    if my_list[index] == target:
        break
    index += 1
else:
    index = -1

print('index:', index)
