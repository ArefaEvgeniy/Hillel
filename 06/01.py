my_list = [1, 2, 3, 4, 5, "df"]
my_list_2 = list((1, 2, 3, 4, 5, "df"))

my_tuple = (1, 2, 3, 4, 5, "df")
my_tuple_2 = tuple((1, 2, 3, 4, 5, "df"))


print(my_list)
print(id(my_list))
print(my_list_2)
print(id(my_list_2))
print(my_tuple)
print(id(my_tuple))
print(my_tuple_2)
print(id(my_tuple_2))

# input_data = [int(item) for item in input("Enter your data with coma: ").split(", ")]
# print(input_data)

# input_data_2 = tuple(int(item) for item in input("Enter your data with coma: ").split(", "))
# print(input_data_2)

t = ("42",)
print(t)
print(type(t))
