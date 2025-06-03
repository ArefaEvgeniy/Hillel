a = []
b = [1,]
c = [4, 6, 'rtre', False, 445, 0, 999]
d = [4, 6, 'rtre', [2, [True, 1, 55], 1], False, 445]

print(type(b))
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(2 in d)

print(d[3][1])
print(d[3][1][len(d[3][1])-1])
print(d[3][1][-2])

print(c[int(len(c)/2)])

list3 = list((3, 4, 77))
list4 = [3, 4, 77]
print(list3)

lst2 = list('Hello world')
print(lst2)
lst3 = ['Hello world']
print(lst3)

if len(c) > 6:
    print(c[6])
