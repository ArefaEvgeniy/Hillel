import json


data = [
    {
        'name': 'Bob',
        'age': 34,
        'hobi': ('boling', 'hunter')
    },
    {
        'name': 'Kite',
        'age': 28,
        'children': ['Mike', 'Susi'],
        'hobi': 'tennis',
        'pets': None
    }
]

with open('test.txt', 'w') as file:
    file.write(str(data))

with open('test_2.json', 'w') as file:
    json.dump(data, file)


for people in data:
    print(people.get('hobi'))
