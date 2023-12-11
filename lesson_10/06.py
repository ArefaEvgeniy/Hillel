# Слово "ciào" якому в кодуванні "utf-8" відповідає b'ci\xc3\xa0o',
# записати в текстовий файл у кодуванні "Latin1".
# Потім прочитати його та вивести на екран.


data = b'ci\xc3\xa0o'
data_str = data.decode()
data_new = data_str.encode('Latin-1')

with open('text_2.txt', 'wb') as f:
    f.write(data_new)

with open('text_3.txt', 'w', encoding='Latin-1') as f:
    f.write(data_str)

with open('text_2.txt', 'rb') as f:
    new_data_1 = f.read().decode('Latin-1')

with open('text_2.txt', 'r', encoding='Latin-1') as f:
    new_data_2 = f.read()

print('new_data_1:', new_data_1)
print('new_data_2:', new_data_2)

# data_2 = "ciào"
#
# with open('text.txt', 'w', encoding='Latin-1') as f:
#     f.write(data_2 + '\n')
#
# with open('text.txt', 'rb') as f:
#     value = f.read().decode('Latin-1')
#
# print(value)
#
# with open('text.txt', 'r', encoding='Latin-1') as f:
#     value_2 = f.read()
#
# print(value_2)
