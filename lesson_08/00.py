my_dict = {3: 2, 1: 5, 4: 9, 5: 23}

for key, value in my_dict.items():
    print(f'Число {key} зустрічається {value} {(lambda x: "парне" if x % 2 == 0 else "не парне")(value)}')


def func_1(x):
    return "парне" if x % 2 == 0 else "не парне"


for key, value in my_dict.items():
    print(f'Число {key} зустрічається {value} {func_1(value)}')


print(my_dict[1])
print(my_dict.get(1, 33))
