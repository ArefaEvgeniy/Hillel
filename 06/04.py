d = {"name": "Alice", "age": 25, "hobbies": ["reading", "writing", "coding"]}
d_1 = {"name": "Tom", "age": 33, "hobbies": ["footbal"]}
d_2 = {"name": "Nick", "age": 12}

print(d)
print(len(d))

print(d["age"])
print(d["name"])
print(d.get("age"))

# print(d["surname"])
print(d.get("surname"))
print(d.get("surname", "key is absent"))
print(d.get("age", "key is absent"))

for item in (d, d_1, d_2):
    hobbies = ", ".join(item["hobbies"]) if "hobbies" in item else "не має"
    print(f"{item['name']} {item['age']}роки, хобі - {hobbies}")
