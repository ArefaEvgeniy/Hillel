my_dict = {"name": "Alice", "name": "Bob", "age": 25, (1, 2, 3): [5, 6, 7], "hobbies": ["reading", "writing", "coding"], 1: 'New value'}

if "children" in my_dict:
    print(my_dict["children"])

print(my_dict.get("children", "цього ключа не має"))

print(my_dict)

my_dict.update({"new_key": "new_value", "new_key_2": "new_value"})
print(my_dict)
