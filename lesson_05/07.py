a = [1, 'a', 'r', 4, 6, 7, 99]

target = 100

for index, item in enumerate(a):
    if str(target) == str(item):
        break
else:
    index = -1

print(f'index: {index}')
