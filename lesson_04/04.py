import datetime

# Запросити у користувача два цілих числа.
# Вивести строку виду "2 плюс 3 дорівнює 5"

a = 2
b = 3

print('% - формотування', end=': ')
now = datetime.datetime.now()
print('%s плюс %s дорівнює %s' % (a, b, a + b))
time1 = datetime.datetime.now() - now

print('метод format', end=': ')
now = datetime.datetime.now()
print('{} плюс {} дорівнює {}'.format(a, b, a + b))
time2 = datetime.datetime.now() - now

print('метод f-string', end=': ')
now = datetime.datetime.now()
print(f'{a} плюс {b} дорівнює {a + b}')
time3 = datetime.datetime.now() - now

print('time1:', time1)
print('time2:', time2)
print('time3:', time3)
