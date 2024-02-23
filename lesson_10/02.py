# Дана змінна artist_bytes у байтовому вигляді.
# Декодувати її в юнікод і вивести на екран.
# Декодування значення закодувати в кодуванні 'Latin1'

artist_bytes = b'Tage \xc3\x85s\xc3\xa9n'

print(len(artist_bytes))
print(type(artist_bytes))
new = artist_bytes.decode('utf-8')
print(new)
print(type(new))

new_2 = new.encode('Latin1')
print(new_2)
print(len(new_2))
print(type(new_2))
