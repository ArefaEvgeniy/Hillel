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
        "completed": None,
        "children": ('Alice', 'Nick')
    },
    {
        "userId": 34,
        "id": 2,
        "score": 2.003,
        "name": "Sam",
        "completed": True
    },
]
