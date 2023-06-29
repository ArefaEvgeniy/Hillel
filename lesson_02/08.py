a = (1, 2, 3)
b = [1, 2, 3]
c = {1, 2, 3, a}
print(c)
d = {"a": 1, "b": 2, 3: "c"}

print(len(d))
print(d.get("a", "Нет такого ключа"))

d_1 = dict()
print(d_1)
d_1.update({'red': 'красный'})
print(d_1)

print(d.keys())
print(d.values())
print(d.items())

aa = d.pop("b")
print(aa)
print(d)
