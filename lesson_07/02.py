# Створити функцію lambda, яка приймає на вхід список імен
# та виводить їх у форматі “Hello, {name}” до іншого списку.
# Всі імена повинні бути написані малими літерами і з великою першою

in_list = ['Tom', 'jerry', 'NIK', 'BoB']

make_list = lambda in_list: [f'Hello, {name.title()}' for name in in_list]
print(make_list(in_list))
