# Создать lambda функцию, которая принимает на вход список имен
# и выводит их в формате “Hello, {name}” в другой список.
# Все имена должны быть написаны строчными буквами и с заглавной первой

in_list = ['Tom', 'JERRY', 'sam', 'KiTe']

make_list = lambda RRR: [f'Hello, {name.title()}' for name in RRR]

print(make_list(in_list))


# def my_func(RRR):
#     return [f'Hello, {name.title()}' for name in RRR]
#
#
# print(my_func(in_list))
