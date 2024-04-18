# Слово "ciào" якому в кодуванні "utf-8" відповідає b'ci\xc3\xa0o',
# записати в текстовий файл у кодуванні "Latin1".
# Потім прочитати його та вивести на екран.

data = b'ci\xc3\xa0o'

with open('t_1.txt', 'wb') as file:
    file.write(data)


with open('t_2.txt', 'w', encoding='utf-8') as file:
    file.write(data.decode())

data_str = data.decode()
data_latin = data_str.encode('latin-1')

with open('t_3.txt', 'wb') as f_1:
    f_1.write(data_latin)

with open('t_3.txt', encoding='latin-1') as f_2:
    print(f_2.read())

with open('t_3.txt', 'rb') as f_3:
    print(f_3.read().decode('latin-1'))
