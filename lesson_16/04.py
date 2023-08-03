def my_generator(low, high):
    while low <= high:
        yield low
        low += 1


a = my_generator(3, 10)

dd = list(a)
print(dd)

try:
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
except StopIteration:
    print('AAAA')

print('-' * 50)

for item in a:
    print(item)
