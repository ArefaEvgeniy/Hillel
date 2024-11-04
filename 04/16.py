from random import randint


lst = []
for _ in range(randint(3, 10)):
    lst.append(randint(1, 100))

print(lst)
