integer = input('Enter your number: ')

if integer.isdigit() and int(integer) > 0:
    print('YES')
else:
    print('Error')
