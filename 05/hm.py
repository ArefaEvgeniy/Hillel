import random


amount = 10
random_lst = []

while amount > 0:
    random_lst.append(random.randint(1, 10))
    amount -= 1

print(random_lst)


amount = 10
random_lst_2 = []
for _ in range(amount):
    random_lst_2.append(random.randint(1, 10))

print(random_lst_2)


random_lst_3 = [random.randint(1, 10) for _ in range(amount)]
print(random_lst_3)
