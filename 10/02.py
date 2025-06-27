def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fibonacci = fibonacci_generator()
for value in fibonacci:
    print(value)
    if value > 1000000:
        break
