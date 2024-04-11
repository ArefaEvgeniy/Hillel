# Є список кличок тварин. Необхідно за допомогою функції map() створити
# новий список в якому перші літери всіх кличок будуть написані з великої
# літери, а решта всіх літер маленькі.
# Можна додати обрізання довгих кличок до 6 символів


my_pets = ['alfred', 'tabitha', 'WiLLiaM', 'Arla', 'REM']


def func(word):
    return word.title()[:6]


my = map(func, my_pets)
print(tuple(my))
print(list(map(lambda word: word.title()[:6], my_pets)))
