# Слово "ciào" якому в кодуванні "utf-8" відповідає b'ci\xc3\xa0o',
# записати в текстовий файл у кодуванні "Latin1".
# Потім прочитати його та вивести на екран.

data = b'ci\xc3\xa0o'
data_str = data.decode()
print(data_str)
with open('test.txt', 'w', encoding="Latin1") as f:
    f.write(data_str)

with open('test.txt', encoding="Latin1") as f:
    new_data = f.read()

print(new_data)

print('-' * 50)

with open('test.txt', 'br') as f:
    new_data_2 = f.read()

print(new_data_2)
print(new_data_2.decode("Latin1"))

print(data_str)
data_latin = data_str.encode("Latin1")
print(data_latin)
with open('test_2.txt', 'wb') as f:
    f.write(data_latin)
