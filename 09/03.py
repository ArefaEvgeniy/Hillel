def apply_operation(operation, data):
    """
    Застосовує вказану операцію до кожного елемента списку.

    :param operation: Функція-операція для застосування.
    :param data: Список даних.
    :return: Результат операції для кожного елемента списку.
    """
    result = []
    for item in data:
        result.append(operation(item))
    return result


# Приклад використання
def square(x):
    return x ** 2


def double(x):
    return x * 2


numbers = [1, 2, 3, 4, 5]

squared_numbers = apply_operation(square, numbers)
doubled_numbers = apply_operation(double, numbers)
squared_numbers_2 = apply_operation(lambda x: x ** 2, numbers)

print(squared_numbers)  # [1, 4, 9, 16, 25]
print(doubled_numbers)   # [2, 4, 6, 8, 10]

# print(help(apply_operation))
# print(help(square))
print(apply_operation.__doc__)
print(double.__doc__)
