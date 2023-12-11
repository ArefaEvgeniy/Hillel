f = open('example.txt')

ss = f.read(10)
print(ss)
ss = f.read(12)
print(ss)
f.seek(5)
ss = f.read(12)
print(ss)

f.close()

print('-' * 50)

with open('example.txt', 'r') as f:
    print(f.readline().strip())
    print(f.readline().strip())
    print(f.readline().strip())

print('-' * 50)

f = open('example.txt')
try:
    ss = f.readlines()
    print(ss)
finally:
    f.close()
