# Ввести два цілих числа A та B.
# Вивести в порядку зростання всі цілі числа,
# розташовані між A і B (включаючи самі числа A і B),
# а також кількість N цих чисел.


value_1 = input('Enter first number: ')
value_2 = input('Enter second number: ')

num_1 = int(value_1) if value_1.isdigit() else 0
num_2 = int(value_2) if value_2.isdigit() else 0

if num_1 > num_2:
    num_1, num_2 = num_2, num_1

N = 0
for item in range(num_1, num_2 + 1):
    print(item, end=' ')
    N += 1

print()
print('N:', N)
