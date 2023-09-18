# Дана змінна artist_bytes у байтовому вигляді.
# Декодувати її в юнікод і вивести на екран.
# Декодування значення закодувати в кодуванні 'Latin1'


artist_bytes = b'Tage \xc3\x85s\xc3\xa9n'
print(type(artist_bytes))
print(len(artist_bytes))

artist_str = artist_bytes.decode()
print(artist_str)
print(type(artist_str))

artist_Latin = artist_str.encode('Latin1')
print(artist_Latin)
print(type(artist_Latin))
print(len(artist_Latin))

print(artist_Latin.decode('Latin1'))
