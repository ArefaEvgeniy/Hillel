# Є набір чисел (float або int). Вам потрібно знайти різницю між найбільшим
# (максимум) і найменшим (мінімум) елементом. Ваша функція difference має
# вміти працювати з невизначеною кількістю аргументів. Якщо аргументів немає,
# то функція повертає 0 (нуль). Якщо з 3-м тестом будуть проблеми,
# використовуйте функцію округлення round(x, 2), де х це число, яке потрібно
# округлити.
#
# Вх. Дані: Змінна кількість аргументів як числа (int, float).
# Вих. Дані: Різниця між максимумом і мінімумом як число (int, float).
#
# Приклади:
# assert difference(1, 2, 3) == 2, 'Test1'
# assert difference(5, -5) == 10, 'Test2'
# assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
# assert difference() == 0, 'Test4'
# print('OK')


def difference(*args: int | float) -> float:
    """ The function returns the difference between two numbers.
    :param args: any positional arguments
    :return: difference between max and min arguments"""

    if not args:
        return 0

    return round(max(args) - min(args), 2)


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
