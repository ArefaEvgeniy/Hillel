s_1 = "Python"
s_2 = "is"
s_3 = "awesome!"
my_string = s_1 + ' ' + s_2 + ' ' + '\t' + s_3 + ' ' + '.'

print(my_string)
print(len(my_string))

print("n is  " in my_string)
print("a" in my_string)

print(my_string[5])
print(my_string[-2])
print(my_string[3:9])
print(my_string[5:-1])
print(my_string[5:])
print(my_string[5::3])


for item in my_string:
    print(item)
