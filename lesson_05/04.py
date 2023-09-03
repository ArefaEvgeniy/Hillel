# Ввести число, перевірити, що було введено саме число.
# Звести його в куб.
# Реалізацію обернути у вічний цикл із можливістю вийти з нього на запит.


while True:
    input_value = input()

    if not input_value.isdigit():
        continue

    print(f'Куб числа {input_value}, дорівнює: {int(input_value) ** 3}')

    answer = input('Бажаєти вийти? (Y/Т): ')
    if answer.upper() in ('Y', 'Т'):
        break
