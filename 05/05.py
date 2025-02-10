my_string_1 = 'I like Py.thon'


print(my_string_1.title())
print(my_string_1)


my_string = "PHI like, PHP,\tPHP,   PHP,"

# можна вказувати кілька методів поспіль
my_string1 = my_string.replace("PHP", "Python").replace(',', '', 2)
print(my_string1)  # виведе: I like Python! Python! Python!

lst = my_string.split()
lst_2 = my_string.split('PH')
print(lst)
print(lst_2)
print(my_string.strip(',HP '))

new_string = " ".join(lst)
print(new_string)
