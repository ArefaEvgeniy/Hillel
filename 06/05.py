dictionary = {1: 34, 'RRR': 66, 6: 'tryt', '0': [1, 2, 0]}

print(dictionary[6])
print(dictionary['0'][1])
if '6' in dictionary:
    print(dictionary['6'])
print(dictionary.get('RRRW', 'Не має такого ключа'))

dictionary.update({5: 'q', 7: 'e', 9: 'tt'})
dictionary.update({(4, 6, 7): 'q'})
print(dictionary)

print('-' * 100)
for item in dictionary:
    print(dictionary[item])
