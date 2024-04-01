age = input('Enter your age: ')

if (age.startswith('-') and age[1:].isdigit()) or age.isdigit():
    print('number')

if not age.isdigit() or int(age) == 0:
    print('error')
elif 0 < int(age) < 10:
    ...
else:
    print('else')
