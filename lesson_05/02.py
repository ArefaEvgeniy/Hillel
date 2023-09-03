lst = [1, 3, 55, 0, 99, 566, 45]

target = 33

index = 0
while index < len(lst):
    if lst[index] == target:
        break
    index += 1
else:
    index = -1

print(f'index: {index}')
