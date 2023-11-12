list_a = ['aa', 'b', 67.55, None, 67.55]

print('b' in list_a)
print(len(list_a))
list_a.append(99)
print(list_a)
list_a.insert(1, 'Hello world')
print(list_a)

d = list_a.remove(67.55)
print(list_a)
print(d)

del list_a[0]
print(list_a)

list_b = [0, 1, 2, 3]
list_a.extend(list_b)
print(list_a)

c = list_a.pop(0)
print(list_a)
print(c)
