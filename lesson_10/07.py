# Слово "ciào" которому в кодировке "utf-8" соответсвует b'ci\xc3\xa0o',
# записать в текстовый файл в кодировке "Latin1".
# Затем прочитать его и вывести на экран.


data = b'ci\xc3\xa0o'
data_str = data.decode()
print(data_str)

with open('new.txt', 'wb') as file:
    file.write(data_str.encode('Latin1'))

with open('new.txt', 'rb') as file:
    new_data = file.read()

print(new_data)
print(new_data.decode('Latin1'))


with open('new_2.txt', 'w', encoding='Latin1') as file:
    file.write(data_str)

with open('new_2.txt', encoding='Latin1') as file:
    new_data_2 = file.read()

print(new_data_2)
