# a = 'string'
# print(a.find('xx'))

my_list = [0, 11, 2, 34, 43, 99]
target = 55

index = 0
while index < len(my_list):
    if my_list[index] == target:
        break
    index += 1
else:
    index = -1

print(index)


for index_2, x in enumerate(my_list):
    if x == target:
        break
else:
    index_2 = -1
print(index_2)
