# Серіалізувати словник у json-формат та зберегти серіалізовані
# дані в файл. А також у рядковий формат без збереження у файл.
# Десиріалізувати записані дані з диска.

import json

input_data = [
  {
    "userId": 1,
    "id": 1,
    "score": 5000.45,
    "name": "Tom",
    "completed": False
  },
  {
    "userId": 34,
    "id": 2,
    "score": None,
    "name": "Sam",
    "completed": True
  },
  {
    "userId": 35,
    "children": (
      {
        "name": "Jesy",
        "age": 5
      },
      {
        "name": "Ken",
        "age": 15
      }
    )
  }
]

with open('task_01.json', 'w') as f:
  json.dump(input_data, f)


with open('task_01.json') as f:
  new_data = f.read()

print(input_data)
print(type(input_data))
print(input_data[0].get('userId'))
print(input_data[1].get('userId'))
print('-' * 50)
print(new_data)
print(type(new_data))
print('-' * 50)

with open('task_01.json') as f:
  new_data_2 = json.load(f)

print(new_data_2)
print(type(new_data_2))
print(new_data_2[1].get('userId'))
