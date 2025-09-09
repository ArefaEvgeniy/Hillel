a = 'Hello'
b = 'World'
c = a + ' ' + b

print(a[0])
print(a[-1])
print(c[::-1])

print(c.upper())
print(c)

while True:
    number = input('Enter a number from 0 to 100: ')
    if number.isdigit():
        number = int(number)
        if 0 <= number <= 100:
            break
        else:
            print('Number is out of range')
    else:
        print('You entered not a number')

...
