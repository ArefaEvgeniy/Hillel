# while True:
#     number = input('Enter your number: ')
#     if number.isdigit() and 0 < int(number) < 100:
#         break
#     print('Wrong input')

n = 5
while n <= 10:  # запускаємо цикл при умові n <= 10
    print(n)  # друкуємо значення n
    n = n + 1  # збільшуємо значення n на 1
    if n == 7:
        break
else:
    print('ELSE')
print('End')
