# Створити функцію lambda, яка приймає на вхід список імен
# та виводить їх у форматі “Hello, {name}” до іншого списку.
# Всі імена повинні бути написані малими літерами і з великою першою

names = ['Bob', 'ken', 'KaIsy', 'TOM']
for item in (lambda my_list: [f'Hello, {x.title()}' for x in my_list])(names):
    print(item)
