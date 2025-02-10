import random


list_new = [random.randint(1, 10) for _ in range(random.randint(3, 10))]
print(list_new)
for item in list_new:
    print(item, end=' ')
print()

a = [1, -2, 33, 56, 23, 0, -34, 67, -100, 1]

b_1 = []
for item in a:
    if item > 0:
        b_1.append(item ** 2)

print(b_1)

b_2 = [item ** 2 for item in a if item > 0]
print(b_2)

b_3 = [(i ** 2 if i % 2 == 0 else i ** 3) for i in a if i > 0]
print(b_3)
