d = {"name": "Alice", "age": 25, "hobbies": ["reading", "writing", "coding"]}

for item in d:
    print(item)

print('-' * 100)

for item in d:
    print(d[item])

print('-' * 100)

for item in d.keys():
    print(item)

print('-' * 100)

for item in d.values():
    print(item)

print('-' * 100)

for item in d.items():
    print(f'{item[0]} - {item[1]}')

print('-' * 100)

for key, value in d.items():
    print(f'{key} - {value}')

d["age"] = 33
print(d)

d["surname"] = "Kruz"
print(d)

d.update({"surname_2": "Red", (1, 2, 3): 0, 2: "Black"})
print(d)
