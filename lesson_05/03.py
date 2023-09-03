lst = [1, 3, 55, 0, 99, 566, 45]

target = 99

for item in enumerate(lst):
    if item[1] == target:
        index = item[0]
        break
else:
    index = -1

print(f'index: {index}')
print(f'item: {item}')
