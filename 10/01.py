def my_generator():
    yield 1
    yield 2
    yield 3
    return None


gen = my_generator()

print(next(gen))  # Вивід: 1
print(next(gen))  # Вивід: 2
print(next(gen))  # Вивід: 3
print(next(gen))
