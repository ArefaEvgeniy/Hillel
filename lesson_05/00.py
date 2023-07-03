while True:
    input_value = input('Enter your number: ')

    if not input_value.isdigit():
        continue

    print(int(input_value) ** 3)

    answer = input('Хотите выйти? (Y/Д): ')
    if answer.upper() in ('Y', 'Д'):
        break
