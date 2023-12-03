# Ввести з клавіатури ціле додатне число n.
# Отримати суму кубів всіх натуральних чисел від 1 до n(включаючи n).
# Винятки становлять усі числа кратні числу 3.
# Реалізувати у 2-х варіантах: використовуючи цикл while та цикл for
#
# Наприклад, якщо введено число 4, то вам потрібно скласти куби чисел
# від 1 до 4, виключаючи 3. Тобто: 1 + 8 + 64 = 73

value = int(input("Enter the value: "))

sum = 0
for i in range(1, value+1):
    if not i % 3 == 0:
        i **= 3
        sum += i
print(f"Total sum: {sum} ")

counter = 0
i = 1
sum = 0
while counter < value:
    counter += 1
    if counter % 3 == 0:
        continue
    i = counter**3
    sum += i
print(f"Total sum: {sum} ")
