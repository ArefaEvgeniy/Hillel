# Дана змінна artist_bytes у байтовому вигляді.
# Декодувати її в юнікод і вивести на екран.
# Декодування значення закодувати в кодуванні 'Latin1'


artist_bytes = b'Tage \xc3\x85s\xc3\xa9n'

artist = artist_bytes.decode()
print(artist)

artist_bytes_2 = artist.encode('Latin-1')
print(artist_bytes_2)

print(len(artist_bytes))
print(len(artist_bytes_2))

artist_2 = artist_bytes_2.decode('Latin-1')
print(artist_2)
