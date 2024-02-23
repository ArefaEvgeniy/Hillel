# Слово "ciào" якому в кодуванні "utf-8" відповідає b'ci\xc3\xa0o',
# записати в текстовий файл у кодуванні "Latin1".
# Потім прочитати його та вивести на екран.

a = b'ci\xc3\xa0o'

with open('test.txt', 'w', encoding='Latin1') as file:
    file.write(a.decode('utf-8'))

with open('test.txt', encoding='Latin1') as file:
    print(file.read())

print('-' * 50)

with open('test.txt', 'wb') as file:
    file.write(a.decode('utf-8').encode('Latin1'))

with open('test.txt', 'rb') as file:
    print(file.read().decode('Latin1'))
