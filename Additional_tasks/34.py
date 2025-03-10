# Напишіть функцію merge_dicts, яка приймає довільну кількість словників 
# як аргументи і повертає новий словник, що об'єднує все вхідні словники. 
# Якщо ключі повторюються, значення мають бути об'єднані в перелік. 
# Функція повинна використовувати аргумент *args або **kwargs для 
# прийняття довільного числа словників.
#
# Приклад введення:
# {'a': 1, 'b': 2}
# {'b': 3, 'c': 4}
# {'c': 5, 'd': 6}
#
# Приклад висновку:
# {'a': [1], 'b': [2, 3], 'c': [4, 5], 'd': [6]}
