import random


my_list = [1, 2, 1000, 3, 10000, -88767, 5, 99, -100, 0, 10001]

print(random.random())
print(random.randint(1, 100))
print(random.choice(my_list))
random.shuffle(my_list)
print(my_list)
