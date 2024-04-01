number = int(input('Enter your number: '))

my_list_1 = []
for item in range(number+1):
    if item % 3 != 0:
        my_list_1.append(item ** 3)

print(my_list_1)

my_list_2 = [x ** 3 for x in range(number+1) if x % 3 != 0]
print(my_list_2)
