def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Виклик генератора Фібоначчі
fibonacci = fibonacci_generator()
for value in fibonacci:
    if value > 1000:
        break
    print(value)
