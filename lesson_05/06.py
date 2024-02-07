# Ввести два цілих числа A та B.
# Вивести в порядку зростання всі цілі числа,
# розташовані між A і B (включаючи самі числа A і B),
# а також кількість N цих чисел.

value1 = input('Enter first number: ')
value2 = input('Enter second number: ')

num1 = int(value1) if value1.isdigit() else 0
num2 = int(value2) if value2.isdigit() else 0

if num1 > num2:
    num1, num2 = num2, num1

n = 0
for item in range(num1, num2 + 1):
    print(item, end=' ')
    n += 1

print()
print(f'N={n}')
