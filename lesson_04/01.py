text = 'Мене звати %s. Мені %s роки. Ім\'я %s класне.'
text2 = 'Мене звати %(name)s. Мені %(age)s роки. Ім\'я %(name)s класне.'
text3 = 'Мене звати %(aa)s. Мені %(bb)s роки. Ім\'я %(aa)s класне.'

print(text % ('Євген', 44, 'Євген'))
print(text2 % {'name': 'Євген', 'age': 44, 'rrr': 99})

name = 'Євген'
age = 44

print(text3 % {'aa': name, 'bb': age})
