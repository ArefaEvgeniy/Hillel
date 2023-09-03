a = 'q'
a_2 = """hElLo wORld."""
a_3 = "49874753"
a_4 = " "

print(len(a_3))
print(len(a_4))

s = None

print(a_2.upper())
print(a_2.title())
print(a_2.capitalize())
print(a_2.lower())
print('-' * 50)
print(a_2)
print('-' * 50)

print(type(a_3))
print(a_3.isdigit())
print(a_2.find('WOR'))

print('-' * 50)

index = a_2.find('wORld')
print(a_2[index:10])
ss = a_2[index::-2]
print(a_2[::-2])

print(ss.upper() + '!!!')

print('hElLo wORld.' in a_2)

a_2.split()
a_2.strip()
a_2.replace()
