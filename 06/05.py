my_dict = {"name": "Alice", "age": 25, (1, 2, 3): [5, 6, 7], "hobbies": ["reading", "writing", "coding"], 1: 'New value'}

print(len(my_dict))

print(my_dict["name"])
print(my_dict["age"])

print('*' * 100)
for key in my_dict:
    print(my_dict[key])

print(my_dict.items())

print('*' * 100)
for item in my_dict.values():
    print(item)

print('*' * 100)
for key in my_dict:
    print(f'{key} - {my_dict[key]}')

print('*' * 100)
for key, value in my_dict.items():
    print(f'{key} - {value}')



