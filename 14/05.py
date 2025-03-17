import json


with open('test.txt') as file:
    new_data = file.read()

print(new_data)
print(type(new_data))


with open('test_2.json') as file:
    new_data_2 = json.load(file)

print(new_data_2)
print(type(new_data_2))


for people in new_data_2:
    print(people.get('hobi'))
