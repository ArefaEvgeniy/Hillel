# Створити функцію lambda, яка приймає на вхід список імен
# та виводить їх у форматі “Hello, {name}” до іншого списку.
# Всі імена повинні бути написані малими літерами і з великою першою

names = ['jack', 'tom', 'JERRY', 'KaiT', 'JOe']


def n_1(names):
    new_names = []
    for item in names:
        new_names.append(f'Hello, {item.title()}')
    return new_names


print(n_1(names))
# n_2 = lambda names, aa: [f'Hello, {item.title()}{aa}' for item in names]
n_2 = lambda names, aa: f'Hello, {names[1].title()}{aa}'
print(n_2(names, '!!!'))
# n_2 = lambda names, aa: ([f'Hello, {item.title()}' for item in names], [f'{item.capitalize()}' for item in aa])
# r_1, r_2 = n_2(names, ['jack', 'KaiT', 'JOe'])
# print(r_1)
# print(r_2)


for index, _ in enumerate(names):
    print(index)
