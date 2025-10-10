first_name = 'Bob'
second_name = ''
last_name = 'Smith'

full_name = first_name + ' ' + second_name + ' ' + last_name

print(full_name)

list_of_names = [x for x in (first_name, second_name, last_name) if x]

full_name_2 = ' '.join(list_of_names)
print(full_name_2)
