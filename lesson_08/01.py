# Є список кличок тварин. Необхідно за допомогою функції map() створити
# новий список в якому перші літери всіх кличок будуть написані з великої
# літери, а решта всіх літер маленькі.
# Можна додати обрізання довгих кличок до 6 символів


my_pets = ['alfred', 'tabitha', 'WiLLiaM', 'Arla', 'REM']

upper_pets = []
for item in my_pets:
    upper_pets.append(item.title())
print(upper_pets)


def my_func(name):
    return name.title()[:6]


upper_pets_2 = list(map(my_func, my_pets))
print(upper_pets_2)

upper_pets_3 = list(map(lambda item: item.title()[:6], my_pets))
print(upper_pets_3)

upper_pets_4 = list(map(str.title, my_pets))
print(upper_pets_4)
