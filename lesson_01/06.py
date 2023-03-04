text_1 = 'Hello'
text_2 = 'world World wORlD World'

print((text_1 + ', ' + text_2) * 2)

print(10 * text_2)

print(len(text_1))
print(len(text_2))
print(len(text_1 + ', ' + text_2))

print((text_1 + ', ' + text_2)[::-2])

text_3 = text_1 + ', ' + text_2

print(text_3)
print(text_3.upper())
print(text_3.lower())

print(text_2.title())
print(text_2.capitalize())

print(42)
print(type(42))
print('42')
print(type('42'))

print('42.4'.isdigit())
print('rr eyf'.isalpha())

print(text_3)
print(text_3.find('WoR'))
