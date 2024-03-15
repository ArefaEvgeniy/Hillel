# Створити генератор, який при ініціалізації приймає 2 значеня: мінімальне та
# максимальне. При кожному зверненні він повинен повертати значення по порядку
# від мінімального до максимального возведеного до квадрату мінус подвоєне значення.

def generator(min_1=0, max_1=100):
    while max_1 >= min_1:
        yield min_1 ** 2 - 2 * min_1
        min_1 += 1


# my_gen = generator(1, 5)
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))

for item in [1, 2, 5, 8, 0, -11]:
    print(item)
