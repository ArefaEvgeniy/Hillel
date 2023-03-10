# Создать lambda функцию, которая принимает на вход список имен
# и выводит их в формате “Hello, {name}” в другой список.
# Все имена должны быть написаны строчными буквами и с заглавной первой

my_list = ['Bob', 'JACK', 'sindy']

make_list = lambda my_pets: [f'Hello, {name.title()}' for name in my_pets]
print(make_list(my_list))
