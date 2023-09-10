# Ввести з клавіатури ціле додатне число n.
# Отримати суму кубів всіх натуральних чисел від 1 до n(включаючи n).
# Винятки становлять усі числа кратні числу 3.
# Реалізувати у 2-х варіантах: використовуючи цикл while та цикл for


value = int(input("Enter the value: "))

sum_1 = 0
for i in range(1, value+1):
    if not i % 3 == 0:
        i **= 3
        sum_1 += i
print(f"Total sum: {sum_1} ")

counter = 0
i = 1
sum_2 = 0
while counter < value:
    counter += 1
    if counter % 3 == 0:
        continue
    i = counter**3
    sum_2 += i
print(f"Total sum: {sum_2} ")
