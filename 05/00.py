japan = '㍿おき'
word = 'ciào'
ukraine = "привітi"

enc_1 = japan.encode('utf-8')
print(enc_1)
print(len(enc_1))
print(enc_1.decode())
print(enc_1.decode("Windows-1251"))
print("-----------------")
enc_2 = word.encode('utf-8')
print(enc_2)
print(len(enc_2))
print("-----------------")
enc_3 = ukraine.encode('utf-8')
print(enc_3)
print(len(enc_3))
print(enc_3.decode('Latin-1'))
