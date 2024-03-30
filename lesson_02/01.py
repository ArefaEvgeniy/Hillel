a = 'heLLo, worLLd!'
c = '3457'

b = a.capitalize()

print(len(a))
print(b)
print(a.title())
print(a)

print(a.lower())
print(a.upper())

print(a.isdigit())
print(c.isdigit())

print(a.isalpha())

print(a.find(','))

print(a.split('LL'))
print(a.strip('he'))

print(a.replace('LL', 'll', 1))

print(a)  # 'heLLo, worLLd!'

print(a[7])
print(a[-1])
print(a[len(a)-1])

print(a[2:10])
print(a[2:-1])
print(a[2:])

print(a[0:5])
print(a[:5])
print(a[0:])
print(a[:])

print(a[0:10:2])

print(a[10:1:-3])
