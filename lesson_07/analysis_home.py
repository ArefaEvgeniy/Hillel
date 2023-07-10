# !!! Это задание выполнять не надо!!!
# Это разбор предыдущего домашнего задания
# Ввести с клавиатуры целое число number.
# Получить сумму кубов всех целых чисел от 1 до number(включая number).
# Исключения составляют все числа кратные цифре 3.
# Реализовать в 2-х вариантах: используя цикл while и цикл for


while True:
    n = input('insert  value')
    if not n.isdigit() or n == 0:
        print('try one more time')
    else:
        n = int(n)

    i = 1
    ksum = 0
    while i <= n:
        if i % 3 == 0:
            continue
        else:
            a = i ** 3
            ksum = a + ksum
            i += 1
    print(ksum)

    m = 1
    ksum = 0
    exception1 = 0
    for n in range(m, n):
        exception1 = n % 3
        if exception1 == 0:
            continue
        a = n ** 3
        ksum = a + ksum
    print(ksum)

    print('Желаете выйти? (Д/Y): ')
    print('Желаете продолжить нажмите Enter: ')
    a = input()
    if a == 'Y':
        break
    elif a == 'Д':
        break
    else:
        continue



while True:
    n = input('insert  value')
    if not n.isdigit() or n == 0:
        print('try one more time')
        continue

    n = int(n)

    i = 1
    ksum = 0
    while i <= n:
        if i % 3 != 0:
            ksum = i ** 3 + ksum
        i += 1

    print(ksum)

    ksum = 0
    for n in range(1, n):
        if n % 3 == 0:
            continue
        ksum = n ** 3 + ksum
    print(ksum)

    print('Желаете выйти? (Д/Y): ')
    print('Желаете продолжить нажмите Enter: ')
    a = input()
    if a.upper() in ('Y', 'Д'):
        break





n = int(input('Enter number: '))
print(n ** 3)

while n > 0:
    if n % 3 == 0:
        print(f'n: {n}')
    n -= 1
