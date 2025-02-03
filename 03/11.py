d = [10, 404, 'Hello', 0, None, False, [34, 55, 'eee', [44, 10, 0], True], 99, 100]
a = [1, 7, 88, 89, 56]

print(d)
print(d[8])
print(d[-1])
print(d[-2])
if len(a) >= 2:
    print(a[-2])

# print(d[-3][3][-1])
# print(type(d[-3]))

if type(d[-2]) == list or type(d[-2]) == tuple:
    print(d[-2][3][-1])

if isinstance(d[-2], (list, tuple)):
    print(d[-2][3][-1])
