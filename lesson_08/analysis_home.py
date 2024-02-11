while True:
    n = input('insert  value')
    if not n.isdigit() or n == 0:
        print('try one more time')
    else:
        n = int(n)

    i = 1
    ksum = 0
    result = 0
    while i <= n:
        if i % 3 == 0:
            continue
        else:
            result = i ** 3
            ksum = result + ksum
            i += 1
    print(ksum)

    m = 1
    ksum = 0
    result = 0
    exception1 = 0
    for n in range(m, n):
        exception1 = n % 3
        if exception1 == 0:
            continue
        result = n ** 3
        ksum = result + ksum
    print(ksum)
    a = 'fff'
    a.endswith()

    print('Желаете выйти? (Д/Y): ')
    print('Желаете продолжить нажмите Enter: ')
    exit_user = input()
    if exit_user in 'Д' or 'Y':
        break
    else:
        continue
