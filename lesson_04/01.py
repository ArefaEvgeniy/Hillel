ss = "Меня зовут %s, мне %s года. %s красивое имя."
ss_2 = "Меня зовут %(name)s, мне %(age)s года. %(name)s красивое имя."

name = 'Jon'
age = '22'

print(ss % (name, age, name))
print(ss_2 % {'name': name, 'age': age})
print("Меня зовут %s, мне %s года. %s красивое имя." % (name, age, name))
