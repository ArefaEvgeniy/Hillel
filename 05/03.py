s_1 = "Python"
s_2 = "is"
s_3 = "awesome!"
my_string = s_1 + '-' + s_2 + '-' + s_3 + 't'

a = my_string.upper()
print(a)
print(my_string)

print(my_string.title())
print(my_string.capitalize())

print('-' * 100)

my_string_2 = "I Like Python"
print(my_string)
print(my_string_2)

print('-' * 100)

print(my_string.rjust(20, "*"))
print(my_string_2.rjust(20, "*"))
print(my_string_2.rjust(5, "*"))

print('-' * 100)

print(my_string.replace('-', ' ', 5))
print(my_string.replace('o', 'a'))
print(my_string.replace('a', '?'))
print(my_string.replace('o', 'a').replace('a', '?').title())
