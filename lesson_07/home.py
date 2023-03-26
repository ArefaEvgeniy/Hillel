# Дан список чисел. Посчитать сколько раз встречается каждое число.
# Использовать для подсчёта функцию.
# Подсказка: для хранения данных использовать словарь (ключ - само число,
# а значение - сколько раз оно встречается). Для проверки нахождения
# элемента в словаре использовать метод get(), либо оператор in.

from random import randint

# Генерация случайного списка
numbers = []
for _ in range(200):
    numbers.append(randint(1, 10))
print("Первоначальный список: ", numbers)


# Вариант 1
def entries_count(sequence: list) -> dict:
    """Функция подсчета кол-ва чисел в списке"""
    result = {}
    for item in sequence:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    return result


suffix_1 = lambda age: "раза" \
    if (str(age)[-1] in "234" and (True if len(str(age)) == 1 else str(age)[-2] != '1')) \
    else "раз"

result = entries_count(numbers)
for item in sorted(result):
    print(f"Число {item} встречается в первоначальном списке "
          f"{result[item]} {suffix_1(result[item])}")


# Вариант 2
print('-' * 50)

suffix_2 = lambda age: "раза" \
    if age % 10 in (2, 3, 4) and age % 100 not in (12, 13, 14) \
    else "раз"

result_2 = {x: numbers.count(x) for x in set(numbers)}
for item in sorted(result_2):
    print(f"Число {item} встречается в первоначальном списке "
          f"{result_2[item]} {suffix_2(result_2[item])}")
