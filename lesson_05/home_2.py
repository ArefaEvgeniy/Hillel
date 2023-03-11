# Ввести с клавиатуры целое положительное число n.
# Получить сумму кубов всех натуральных чисел от 1 до n(включая n).
# Исключения составляют все числа кратные числу 3.
# Реализовать в 2-х вариантах: используя цикл while и цикл for


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
