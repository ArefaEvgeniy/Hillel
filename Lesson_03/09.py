d = [1, 2, 3, [None, 4.6, 5, 'a'], [True, 'b', [5, 55, 667], 'c'], None, 'Hellow, world!']
b = [1, 2, 3]
c = [1, '66', 'ER', 66, 79, 12, 11, 1, 0, 5]

print(len(d))
print(d[4][2][-1])

if len(d) > 20:
    print(d[20])

print(d[len(d)-2])
print(d[-2])

print(c[1:9])
print(c[0:5])
print(c[:5])
print(c[5:])
print(c[:])
print(c[:7:3])
print(c[-2:1:-2])
print(c[1:-2:-2])
print(c[-2:-2:2])
print(c[-1::-1])
print(c[::-1])

res = []
b = [1, 2, 3]
d = [5, 1, 3]

b.extend(d)
print(b)

res.append(b)
res.append(d)
print(res)

res_2 = [b, d]
print(res_2)

f = 5 // 2
print(f)
