# Дана змінна artist_bytes у байтовому вигляді.
# Декодувати її в юнікод і вивести на екран.
# Декодуваннe значення закодувати в кодуванні 'Latin1'


artist_bytes = b'Tage \xc3\x85s\xc3\xa9n'
print(artist_bytes)
print(len(artist_bytes))

artist_str = artist_bytes.decode()
print(artist_str)
print(len(artist_str))

artist_latin = artist_str.encode('Latin-1')
print(artist_latin)
print(len(artist_latin))
