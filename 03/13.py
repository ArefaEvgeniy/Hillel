a_1 = [34, 67.334, True, ['a', 'b', 34], 'Hello']

a_1.insert(1, 111)
print(a_1)

a_1[2] = [6666, 'ty']
print(a_1)

a_1.pop()
print(a_1)
c = a_1.pop()
print(c)
a_1.pop(0)
print(a_1)

index = 10
if len(a_1) > index:
    a_1.pop(10)

a_1.append(111)
print(a_1)
d = a_1.remove(111)
print(a_1)
print(d)
