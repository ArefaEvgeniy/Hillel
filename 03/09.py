age = input('Enter you age: ')
c = 10

if not age.isdigit() or int(age) == 0:
    print('Incorrect data')
elif int(age) <= 10:
    print('0-10')
elif int(age) <= 20:
    print('10-20')
elif int(age) <= 100:
    print('20-100')
else:
    print('more 100')


if int(age) == 0 and c > 0:
    ...
