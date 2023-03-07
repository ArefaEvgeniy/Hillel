# !!! Это задание выполнять не надо!!!
# Это разбор предыдущего домашнего задания
# Ввести с клавиатуры целое число n.
# Получить сумму кубов всех целых чисел от 1 до n(включая n).
# Исключения составляют все числа кратные цифре 3.
# Реализовать в 2-х вариантах: используя цикл while и цикл for


while True:
    digit1 = input('insert  value')
    if not digit1.isdigit() or digit1 == 0:
        print('try one more time')
    else:
        digit1 = int(digit1)

    # Операторы циклов While
    index = 1
    result = 0
    while index <= int(digit1):
        if index % 3 != 0:
            result += index ** 3
            index += 1

    # Оператор For
    ksum = 0
    exception1 = 0
    for digit1 in range(digit1):
        exception1 = digit1 % 3
        if exception1 == 0:
            continue
        a = digit1 ** 3
        ksum = a + ksum
        if digit1 <= 0:
            break
    print(ksum)

    print('Желаете выйти? (Д/Y): ')
    print('Желаете продолжить нажмите Enter: ')
    answer = input()
    if answer == 'y' or answer == 'Y' or answer == 'д' or answer == 'Д':
        break
    else:
        continue



while True:
    digit1 = input('insert  value')
    if not digit1.isdigit() or digit1 == 0:
        print('try one more time')
        continue
    digit1 = int(digit1)

    # Операторы циклов While
    result = 0
    while digit1 > 0:
        if digit1 % 3 != 0:
            result += digit1 ** 3
        digit1 -= 1

    # Оператор For
    ksum = 0
    for item in range(digit1):
        if item % 3 != 0:
            ksum += item ** 3

    print(ksum)

    print('Желаете выйти? (Д/Y): ')
    print('Желаете продолжить нажмите Enter: ')
    answer = input()
    if answer.upper() in ('Y', 'Д'):
        break
    else:
        continue
