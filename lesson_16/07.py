def func(a):
    while a < 100:
        yield 2 * a
        a *= 5


# my_a = func(2)
# print(my_a)
# print(next(my_a))
# print(next(my_a))
# print(next(my_a))
# print(next(my_a))
# print(next(my_a))

for item in func(2):
    print(item)
