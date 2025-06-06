while True:
    number = input('Enter your number(1-10): ')
    if number.isdigit() and 0 < int(number) < 11:
        break
    print('Wrong enter. Repeat, please')

print('number:', number)
