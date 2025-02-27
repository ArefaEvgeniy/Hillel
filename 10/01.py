def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fibonacci = fibonacci_generator()
for value in fibonacci:
    print(value)
    if value > 1000:
        break

print('-' * 100)
fibonacci_2 = fibonacci_generator()
print(next(fibonacci_2))
print(next(fibonacci_2))
print(next(fibonacci_2))
print(next(fibonacci_2))
print(next(fibonacci_2))
