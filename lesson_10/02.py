# Дана переменная artist_bytes в байтовом виде.
# Декодировать её в юникод и вывести на экран.
# Декодирование значение закодировать в кодировке 'Latin1'


artist_bytes = b'Tage \xc3\x85s\xc3\xa9n'
print(artist_bytes)
print(len(artist_bytes))
artist = artist_bytes.decode()
print(artist)

artist_latin = artist.encode('Latin1')
print(artist_latin)
print(len(artist_latin))
print(artist_latin.decode('Latin1'))

# japan_char = 'ぁ'
# japan_latin = japan_char.encode('Latin1')
# print(japan_latin)
