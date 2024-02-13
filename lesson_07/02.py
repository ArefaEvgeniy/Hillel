# Створити функцію lambda, яка приймає на вхід список імен
# та виводить їх у форматі “Hello, {name}” до іншого списку.
# Всі імена повинні бути написані малими літерами і з великою першою

list_name = ['KAT', 'nick', 'BoB', 'roB']
new_list = ['ЄВГЕН', 'окСана', 'микола']


def func(in_list):
    return [f'Hello, {i.title()}' for i in in_list]


make_list = lambda in_list: [f'Hello, {i.title()}' for i in in_list]

print(make_list(list_name))
print(make_list(new_list))
