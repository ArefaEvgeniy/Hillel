# Сериализовать словарь в json-формат и сохранить сериализованные
# данные в файл. А также в строковый формат без сохранения в файл.
# Десириализовать записанные данные с диска.


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
    "score": 2.003,
    "name": "Sam",
    "hobbies": ("running", "tennis"),
    "relation": None,
    "completed": True
  },
]

with open('01.json', 'w') as file:
  json.dump(input_data, file)


with open('01.json') as file:
  new_data = json.load(file)

print('new_data:', new_data)
print('type:', type(new_data))

print('input_data.score:', input_data[0].get("score"))
print('input_data.score:', new_data[0].get("score"))
