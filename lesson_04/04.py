# Запросити у користувача два цілих числа.
# Вивести строку виду "2 плюс 3 дорівнює 5"

import datetime


num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

print('%-format', end=': ')
now = datetime.datetime.now()
print("%s plus %s = %s" % (num_1, num_2, num_1 + num_2))
print("spend time: ", datetime.datetime.now() - now)

print('method .format()', end=': ')
now = datetime.datetime.now()
print("{} plus {} = {}".format(num_1, num_2, num_1 + num_2))
print("spend time: ", datetime.datetime.now() - now)

print('f-string', end=': ')
now = datetime.datetime.now()
print(f"{num_1} plus {num_2} = {num_1 + num_2}")
print("spend time: ", datetime.datetime.now() - now)
