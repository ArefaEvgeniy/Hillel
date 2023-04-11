def simple_generator(value):
    current = 1
    while current < value:
        yield current
        current += 2


res = simple_generator(50)
for item in res:
    print(item)
