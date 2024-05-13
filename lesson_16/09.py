def my_func(first, step):
    res = first
    while True:
        res *= step
        yield res


b = my_func(3, 6)
print(b)

for item in b:
    print(item)
    if item > 1000:
        break

print(next(b))
print(next(b))
