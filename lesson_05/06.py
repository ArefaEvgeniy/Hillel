# Ввести два цілих числа A та B.
# Вивести в порядку зростання всі цілі числа,
# розташовані між A і B (включаючи самі числа A і B),
# а також кількість N цих чисел.

value1 = input('Enter first number: ')
value2 = input('Enter second number: ')

num_1 = int(value1) if value1.isdigit() else 0
num_2 = int(value2) if value2.isdigit() else 0

if num_1 > num_2:
    num_1, num_2 = num_2, num_1

N = 0
for item in range(num_1, num_2+1):
    end = ', ' if item != num_2 else '\n'
    print(item, end=end)
    N += 1

print('N =', N)
