def my_generator(n, m):
    for _ in range(m):
        yield n ** 2
        n += 1


for value in my_generator(2, 4):
    print(value)
