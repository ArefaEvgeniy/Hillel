# Даний рядок у байтовому вигляді: b'r\xc3\xa9sum\xc3\xa9' закодована в
# кодуванні за умовчанням utf-8.
# Декодувати її у рядковий вигляд у кодуванні за замовчуванням.
# Потім результат знову перетворити на байтовий, тільки вже в кодуванні 'Latin1'
# І на кінець результат знову декодувати у рядок
# (Результати всіх перетворень виводити на екран).

input_data = b'r\xc3\xa9sum\xc3\xa9'
print(input_data)
data_1 = input_data.decode()
print(data_1)
data_2 = data_1.encode('Latin1')
print(data_2)
data_3 = data_2.decode('Latin1')
print(data_3)
