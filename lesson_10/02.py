# Дана переменная artist_bytes в байтовом виде.
# Декодировать её в юникод и вывести на экран.
# Декодирование значение закодировать в кодировке 'Latin1'


artist_bytes = b'Tage \xc3\x85s\xc3\xa9n'

print(type(artist_bytes))

print(artist_bytes)
print(f'len of artist_bytes: {len(artist_bytes)}')
artist = artist_bytes.decode('utf-8')
print(artist)
print(f'len of artist: {len(artist)}')

print('-' * 50)

artist_latin1 = artist.encode('Latin1')
print(artist_latin1)
print(f'len of artist_latin1: {len(artist_latin1)}')
