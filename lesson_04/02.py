template_1 = "Мене звати {}. Мені {} роки. {} класно ім'я"
template_2 = "Мене звати {name_2}. Мені {age_3} роки. {name_2} класно ім'я"
template_3 = "Мене звати {0}. Мені {1} роки. {0} класно ім'я"
name = "Євген"
age = 44

print(template_1.format(name, age, name))
print(template_2.format(age_3=age, name_2=name))
print(template_3.format(name, age))

coord = (3, 5)
print('X:{1[0]}, Y:{1[1]}'.format(55, coord))

print('{:-^30}'.format('Євген'))

print('{:.5%}'.format(35/178))
