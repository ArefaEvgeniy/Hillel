# Запитати у користувача вік.
# Якщо вік менше 0 або введено не число – вивести Wrong input
# Якщо вік менше або дорівнює 12 - вивести Orange
# Якщо вік більше 12 і менше 18 - вивести CocaCola
# Інакше - вивести Beer

age = input('Enter your age: ')

if not age.isdigit() or int(age) <= 0:   # False or False -> False
    print('Wrong input')                 # False or True -> True
elif int(age) <= 12:                     # True or False -> True
    print('Orange')                      # True or True -> True
elif int(age) < 18:
    print('CocaCola')                    # False and False -> False
else:                                    # False and True -> False
    print('Beer')                        # True and False -> False
                                         # True and True -> True
