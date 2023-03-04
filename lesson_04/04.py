# Запросить у пользователя два целых числа.
# Вывести строку вида “2 плюс 3 равно 5”

import datetime

num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))

NOW = datetime.datetime.now()
print('Процентное форматирование: %d плюс %d равно %d' % (num_1, num_2, num_1 + num_2))
time_spend_1 = datetime.datetime.now() - NOW

NOW = datetime.datetime.now()
print('Метод format: {} плюс {} равно {}'.format(num_1, num_2, num_1 + num_2))
time_spend_2 = datetime.datetime.now() - NOW

NOW = datetime.datetime.now()
print(f'f-string: {num_1} плюс {num_2} равно {num_1 + num_2}')
time_spend_3 = datetime.datetime.now() - NOW

print()
print('time_spend_1:', time_spend_1)
print('time_spend_2:', time_spend_2)
print('time_spend_3:', time_spend_3)
