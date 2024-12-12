# Напишіть функцію-генератор generate_cube_numbers, яка формує набір кубів
# чисел, починаючи з числа 2 до вказаної Вами величини. Тобто. генератор
# повинен працювати доти, поки генерується значення менше зазначеної величини.
# Нагадую, що вийти із генератора можна за допомогою return без параметрів.
#
# def generate_cube_numbers(end):
#     pass
#
# from inspect import isgenerator
#
# gen = generate_cube_numbers(1)
# assert isgenerator(gen) == True, 'Test0'
# assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
# assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
# assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'

def generate_cube_numbers(end):
    i = 2
    while i ** 3 <= end:
        yield i ** 3
        i += 1


from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
print('ok')
