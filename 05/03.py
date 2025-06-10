my_string = "Beautiful is     better\t than    ugly"

index = my_string.find("e")
print(my_string.find("e", index+1))  # Beautiful is better than ugly
print(my_string[index+1:].find("e"))  # autiful is better than ugly

new_list = my_string.split()
print(new_list)

new_list_2 = my_string.split("e")
print(new_list_2)

new_list_3 = my_string.split("e", 2)
print(new_list_3)

new_list_4 = my_string.split("y")
print(new_list_4)

print(new_list)

new_str = "---".join(new_list)
print(new_str)
