my_dictionary = {"key1": 1, "key2": None, 45: "World", "key": "ключ", "brother": "брат", "sister": "сестра"}

word = my_dictionary.pop("key2")

print(my_dictionary)
print(word)

my_dictionary.update({"key2": None, "key3": 300})
print(my_dictionary)
print(my_dictionary["key"])
if "key5" in my_dictionary:
    print(my_dictionary["key5"])

if "World" in my_dictionary.values():
    print("Yes")
else:
    print("No")

print(my_dictionary.get("key1", "Not found"))
print(my_dictionary.get("key2", "Not found"))
print(my_dictionary.get("key5", "Not found"))

print("-" * 20)
for key, value in my_dictionary.items():
    print(f"Ключ: {key}, значение: {value}")

print("-" * 20)
for key in my_dictionary:
    print(f"Ключ: {key}, значение: {my_dictionary[key]}")
