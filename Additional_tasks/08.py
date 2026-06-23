# Напишіть програму, яка запитує користувача три числа і виводить їх у порядку 
# зростання, розділені комою. Використовуйте умовні оператори та вкладені 
# умови для вирішення завдання. Передбачається, що це три числа різні.

# Приклад:
# Введіть перше число: 5
# Введіть друге число: 2
# Введіть третє число: 7

# Числа в порядку зростання: 2, 5, 7


first_number = int(input('Введіть перше число: '))
second_number = int(input('Введіть друге число: '))
third_number = int(input('Введіть третє число: '))

if first_number > second_number:
    first_number, second_number = second_number, first_number
if second_number > third_number:
    second_number, third_number = third_number, second_number
if first_number > second_number:
    first_number, second_number = second_number, first_number

print(f'Числа в порядку зростання: {first_number}, {second_number}, {third_number}')
