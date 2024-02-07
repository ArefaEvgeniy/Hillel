# Ввести число, перевірити, що було введено саме число.
# Звести його в куб.
# Реалізацію обернути у вічний цикл із можливістю вийти з нього на запит.

while True:
    input_value = input('Enter your number: ')

    if not input_value.isdigit():
        continue

    print(f'КУБ ЧИСЛА: {int(input_value) ** 3}')

    answer = input('Бажаєте вийти? (Д/Y): ')
    if answer.upper() in ('Д', 'Y'):
        break

