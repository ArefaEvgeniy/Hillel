while True:
    n = input('insert  value')
    if not n.isdigit() or n == '0':
        print('try one more time')
        continue
    else:
        n = int(n)

    i = 1
    ksum = 0
    while i <= n:
        if i % 3 != 0:
            ksum = i ** 3 + ksum
        i += 1
    print(ksum)

    m = 1
    ksum = 0
    for n in range(m, n):
        if n % 3 != 0:
            ksum = n ** 3 + ksum
    print(ksum)

    print('Желаете выйти? (Д/Y): \nЖелаете продолжить нажмите Enter: ')
    print('Желаете выйти? (Д/Y): ', 'Желаете продолжить нажмите Enter: ', sep='\n')
    a = input()
    if a in ('Y', 'Д'):
        break
