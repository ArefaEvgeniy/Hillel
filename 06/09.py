a = [1, 55, 33, 45, 38, 0, 20]

new_list = [x * 2 for x in a if x % 2 == 0]
print(new_list)

new_list = (x * 2 for x in a if x % 2 == 0)
print(tuple(new_list))

new_list = {str(x): x * 2 for x in a if x % 2 == 0}
print(new_list)
