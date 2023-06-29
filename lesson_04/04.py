# Запросить у пользователя два целых числа.
# Вывести строку вида “2 плюс 3 равно 5”

import datetime

num_1 = 10
num_2 = 33

now = datetime.datetime.now()
print('%s плюс %s равно %s' % (num_1, num_2, num_1 + num_2))
print(f'время % форматирования: {datetime.datetime.now() - now}')

now = datetime.datetime.now()
print('{} плюс {} равно {}'.format(num_1, num_2, num_1 + num_2))
print(f'время format: {datetime.datetime.now() - now}')

now = datetime.datetime.now()
print(f'{num_1} плюс {num_2} равно {num_1 + num_2}')
print(f'время f-string: {datetime.datetime.now() - now}')
