def func_1():
    a = 10
    while True:
        yield a
        a += 1


s = func_1()
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))

print('-' * 100)
z = func_1()
for item in z:
    print(item)
    if item > 25:
        break

print('-' * 100)
print(next(s))
