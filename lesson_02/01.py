a = 'Hello world'
print(len(a))

print(a[0])
print(a[4])
print(a[10])
print(a[-1])
print(a[-2])

print(a[0:7])
print(a[:7])
print(a[1:-1])
print(a[1:len(a)])
print(a[1:])
print(a[1:9:2])
print(a[1:10:3])
print(a[1::3])
print(a[8::-2])
print(a[::-1])

print(a.lower())
print(a.upper())

b = ' red bLAck green'
c = '43'
d = 43
print(b.title())
print(b.capitalize())

print(b.isdigit())
print(c.isdigit())

print(b.isalpha())

print(b.strip())
print(a.strip('rld'))
print(b.strip('rld'))
print(b.strip('Ack'))

print(a.split())
print(b.split('r'))
print(b.split('bLA'))
