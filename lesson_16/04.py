def simple_generator(value):
    while value > 0:
        value -= 1
        yield 1


res = simple_generator(5)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
