my_list = [1, 2, 1000, 3, 4, -88767, 5, 99, -100, 0, 10001]

number = None
for item in my_list:
    if number is None or item > number:
        number = item
else:
    print("Maximum number calculation is complete.")

print(number)
print(max(my_list))

number_2 = None
index = 0
while index < len(my_list):
    item = my_list[index]
    if number_2 is None or item > number_2:
        number_2 = item
    index += 1

print(number_2)
