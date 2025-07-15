import json

from lesson_01 import Person


with open('data.json') as file:
    data = json.load(file)

print(data)
print(type(data))

data_objects = []
for item in data:
    data_objects.append(Person(item['name'], item['surname'], item['age']))

print(data_objects)
print(data_objects[-1].get_age())
