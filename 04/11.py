my_list = [1, 2, 1000, 3, 10000, -88767, 5, 99, -100, 0, 10001]
# my_list = [-100, -1120, -445, -99877]

number = None
index_number = None
index = 0
for item in my_list:
    if number is None or item > number:
        number = item
        index_number = index
    index += 1

print('Maximum number is:', number, 'and its index is:', index_number)


number = None
index_number = None
for index_2, item in enumerate(my_list):
    if number is None or item > number:
        number = item
        index_number = index_2

print('Maximum number is:', number, 'and its index is:', index_number)
