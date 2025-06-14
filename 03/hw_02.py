# Ваша програма має перенести останній елемент списку з кінця на початок,
# тобто, останній елемент списку має стати першим. Послідовність інших
# елементів не має змінюватися. Порожній список або список з одним елементом
# повинен залишитися незмінним. Кількість елементів у списку може бути
# будь-яким – нуль та більше!

# Приклади:
# [12, 3, 4, 10] => [10, 12, 3, 4]
# [1] => [1]
# [] => []
# [12, 3, 4, 10, 8] => [8, 12, 3, 4, 10]

# Для перевірки коректності роботи Вашого коду використовуйте приклади вище.
# Робити запит на введення даних від користувача не потрібно.


input_list = input("Введіть елементи списку через пробіл: ").split()
if len(input_list) > 1:
    input_list.insert(0, input_list[-1])
    del input_list[-1]

print(input_list)
