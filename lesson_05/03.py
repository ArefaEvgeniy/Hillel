# Ввести число, перевірити, що було введено саме число.
# Звести його в куб.
# Реалізацію обернути у вічний цикл із можливістю вийти з нього на запит.

while True:
    input_value = input('Enter your number: ')

    if not input_value.isdigit():
        print('Wrong input')
        continue

    print('Cube of your number:', int(input_value) ** 3)

    answer = input('do you wan\'t exit? (y/д/Y/Д)').upper()
    if answer in ('Y', 'Д'):
        break
