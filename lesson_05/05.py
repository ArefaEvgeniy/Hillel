my_list = [1, 3, 4, 'tty', 'frd', 6, 99]
target = 'ttyz'

index = 0
for item in my_list:
    if item == target:
        break
    index += 1
else:
    index = -1

print('index:', index)
print('item:', item)

# print('-' * 50)
#
# a = [1, 'e', 't', 'yyt', 0]
# for item in enumerate(a):
#     print(item)

print('-' * 50)

my_list = [1, 3, 4, 'tty', 'frd', 6, 99]
target = 'tty'

for item in enumerate(my_list):
    print('item:', item)
    if item[1] == target:
        index = item[0]
        break
else:
    index = -1

print('index:', index)
print('item:', item[1])

