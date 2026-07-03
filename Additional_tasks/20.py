# Напишіть програму, яка запитує у користувача суму у євро і потім виводить:
# мінімальну кількисть купюр та мінімальну кількість монет для того, щоб
# отримати цю суму у євро. Зверніть увагу на те, що банкноти євро мають
# номінали: 5, 10, 20, 50, 100, 200 та 500 евро. А монети: 1 та 2 євро,
# 1, 2, 5, 10, 20 та 50 євроцентів.
# Крім того треба надрукувати кількість кожного номіналу котрий
# використовується для отримання даної суми.
# * Бажано, щоб суму можна було вводити як через крапку так і через кому.

# Приклад: Введіть суму: 347,78
# Кількість банкнот: 5
# Кількість монет: 7
# Склад суми:
# 1 x 200
# 1 x 100
# 2 x 20
# 1 x 5
# 2 x 1
# 1 x 0.5
# 1 x 0.2
# 1 x 0.05
# 1 x 0.02
# 1 x 0.01


summa = float(input("Введіть суму: ").replace(',', '.'))
summa_euros = int(summa)
summa_cents = round((summa - summa_euros) * 100)

banknotes = [500, 200, 100, 50, 20, 10, 5]
coins = [1, 2, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

number_of_banknotes = 0
number_of_coins = 0
result = ['Склад суми:',]

remainder = summa_euros
for item in banknotes:
    number = remainder // item
    remainder %= item
    if number > 0:
        number_of_banknotes += number
        result.append(f'{number} x {item}')
    if remainder == 0:
        break

remainder = (remainder * 100) + summa_cents
for item in coins:
    number = remainder // (int(item * 100))
    remainder %= (int(item * 100))
    if number > 0:
        number_of_coins += number
        result.append(f'{number} x {item}')
    if remainder == 0:
        break

print('Кількість банкнот:', number_of_banknotes)
print('Кількість монет:', number_of_coins)
if len(result) > 1:
    print('\n'.join(result))
