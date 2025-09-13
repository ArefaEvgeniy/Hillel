b = [3, '444', 67, '353', 3, 55, 9, "pp", 0, 3, 67, '353', 67, 3, '444', 9, 55, 'pp', 0, 3, 67, 900, 900, 'pp']

c = []
for i in b:
    if i not in c:
        c.append(i)

print(c)

d = list(set(b))
print(d)
