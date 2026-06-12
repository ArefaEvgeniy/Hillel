from collections import defaultdict


dct = defaultdict(lambda: 0)

print(dct)
print(len(dct))

print("-" * 20)
dct.update({"key1": 1, "key2": 2})
print(dct)
print(len(dct))

print("-" * 20)
print(dct["key3"])
print(dct)
print(len(dct))

print("-" * 20)
print(dct["key3"])
print(dct)
print(len(dct))

print("-" * 20)
print(dct["key4"])
print(dct)
print(len(dct))

dct["key5"] += 1
