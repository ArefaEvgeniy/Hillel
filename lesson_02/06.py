dict_1 = {1: 'ert', 2: 1234, 3: [1, 2, 3, 4], 4: [1, 2, 3, 4], 'Cat': 0}

print(type(dict_1))
print(len(dict_1))

print(dict_1[1])
print(dict_1[4])
print(dict_1[3])
print(dict_1['Cat'])
print(dict_1.get('Cats', 'такого ключа не має'))
dict_1.update({'Cats': '45'})
print(dict_1.get('Cats', 'такого ключа не має'))
print(dict_1)
value = dict_1.pop('Cat')
print(dict_1)
print(value)

dictionary = {'Я': 'I', 'маю': 'have', 'коробку': 'box'}

a = 'Я маю коробку'
a = a.replace('Я', dictionary['Я'])
a = a.replace('маю', dictionary['маю'])
a = a.replace('коробку', dictionary['коробку'])

print(a)

print(dict_1.keys())
print(dict_1.values())
print(dict_1.items())
