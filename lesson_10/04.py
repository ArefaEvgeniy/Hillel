with open('example.txt') as f:
    a_1 = f.readline()
    a_2 = f.readline()

print(a_1)
print(type(a_1))
print(a_2)
print(type(a_2))

with open('example.txt') as f:
    a = f.readlines()

print(a)
print(type(a))
