# Запитати у користувача вік.
# Якщо вік менше 0 або введено не число – вивести Wrong input
# Якщо вік менше або дорівнює 12 - вивести Orange
# Якщо вік більше 12 і менше 18 - вивести CocaCola
# Інакше - вивести Beer

age = input('Введить ваш вік: ')

if not age.isdigit() or int(age) <= 0:
    print('Wrong input')
elif int(age) <= 12:
    print('Orange')
elif int(age) < 18:
    print('CocaCola')
else:
    print('Beer')
