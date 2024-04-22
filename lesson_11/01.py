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

for item in input_data:
  if item.get("id") and item["id"] == 2:
    print(item.get("name"))
    break
else:
  print('People is absent')

with open('task_01.txt', 'w') as file:
  file.write(str(input_data))

with open('task_01.txt') as file:
  new_dat = file.read()

print(new_dat)
print(type(new_dat))
print(new_dat[:5])

print('-' * 50)

with open('task_01.json', 'w') as file:
  json.dump(input_data, file)

with open('task_01.json') as file:
  new_data_2 = json.load(file)

print(new_data_2)
print(type(new_data_2))

for item in new_data_2:
  if item.get("id") and item["id"] == 2:
    print(item.get("name"))
    break
else:
  print('People is absent')
