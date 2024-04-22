import json

data = {'name': 'Bob', 'children': ['Alice', 'Mike', {1: 2, 3: 4}]}

new_data = json.dumps(data)

print(new_data)
print(type(new_data))

python_data = json.loads(new_data)
print(python_data)
print(type(python_data))
