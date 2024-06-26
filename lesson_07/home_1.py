# Наведено список чисел. Порахувати скільки разів трапляється кожне число.
# Використовувати функцію підрахунку.
# Підказка: для зберігання даних використовувати словник (ключ - саме число,
# а значення - скільки разів воно трапляється). Для перевірки знаходження
# елемента у словнику використовувати метод get(), або оператор in.
# *Додаткові не обов'язкові умови:
#   - Початковий список розміром 200 елементів формується з чисел
#     від 1 до 10 включно взятих випадковим чином;
#   - сформувати підсумковий словник (де ключ це саме число, а значення це
#     у повторень даного числа в первісному списку) за допомогою
#     конструкції "генератор словників";
#   - підсумковий висновок відсортувати по порядку зростання числа, наприклад:
#       Число 1 зустрічається у первісному списку 10 разів
#       Число 2 зустрічається у початковому списку 3 рази
#       Число 3 зустрічається у початковому списку 14 разів
#       Число 4 зустрічається у початковому списку 1 раз
#       і т.д.
#   - використовувати лямбда-функцію для того, щоб визначити яке слово треба
#     написати для конкретного числа: "раз", "разів" або "раза"
#
# from random import randint

from random import randint

# Генерація випадкового списку
numbers = []
for _ in range(200):
    numbers.append(randint(1, 10))
print("Початковий список: ", numbers)


# Варіант 1
def entries_count(sequence: list) -> dict:
    """Функція підрахунку кіл-ва чисел у списку"""
    result = {}
    for item in sequence:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    return result


suffix_1 = lambda age: "раза" if (str(age)[-1] in "234" and (True if len(str(age)) == 1 else str(age)[-2] != '1')) else "раз" if str(age)[-1] == "1" else "разів"

result = entries_count(numbers)
for item in sorted(result):
    print(f"Число {item} зустрічається у первісному списку "
          f"{result[item]} {suffix_1(result[item])}")


# Варіант 2
print('-' * 50)

suffix_2 = lambda age: "раза" if age % 10 in (2, 3, 4) and age % 100 not in (12, 13, 14) \
    else "раз" if str(age)[-1] == "1" else "разів"

result_2 = {x: numbers.count(x) for x in set(numbers)}
for item in sorted(result_2):
    print(f"Число {item} зустрічається у первісному списку "
          f"{result_2[item]} {suffix_2(result_2[item])}")
