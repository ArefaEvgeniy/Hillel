# Слово "ciào" которому в кодировке "utf-8" соответсвует b'ci\xc3\xa0o',
# записать в текстовый файл в кодировке "Latin1".
# Затем прочитать его и вывести на экран.


data = b'ci\xc3\xa0o'
data_2 = data.decode()
data_3 = data_2.encode('Latin1')
print(data_3)

with open('06.txt', 'w', encoding='Latin1') as file:
    file.write(data.decode())

with open('06.txt', encoding='Latin1') as file:
    print(file.read())

file.seek()
file.tell()
