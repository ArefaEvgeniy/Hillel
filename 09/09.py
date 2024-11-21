names = ['Alice', 'Bob', 'Charlie']
ages = (25, 30, 22, 66, 80)
numbers = {'45', '66', '12', '100'}
phone = {'1': 11, '2': 22}

print(list(zip(names, ages)))
print(tuple(zip(names, ages, numbers)))
print(set(zip(names, ages, numbers, phone)))

