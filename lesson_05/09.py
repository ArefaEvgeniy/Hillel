a = []
for i in range(1, 16):
    a.append(i)
print('a:', a)


b = [i**2 for i in range(1, 16)]
print('b:', b)

x = (1, 2, 'f', 't', None, 55, True)
y = [str(i) for i in x]
print('y:', y)

z_1 = [i ** 3 for i in x if type(i) == int]
print('z_1:', z_1)

z_2 = [int(i) ** 3 for i in y if i.isdigit()]
print('z_2:', z_2)

z_3 = {i ** 3 for i in x if type(i) == int}
print('z_3:', z_3)

z_4 = {str(i): i ** 2 for i in x if type(i) == int}
print('z_4:', z_4)

z_5 = {i: int(i) ** 2 for i in y if i.isdigit()}
print('z_5:', z_5)
