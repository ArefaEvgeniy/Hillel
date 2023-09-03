a = []
for i in range(1, 15):
    a.append(i ** 2)

print(a)


print([i ** 2 for i in range(1, 15)])

a = {6: 10, 2: 20, 3: 30}

b = (i * a[i] for i in a)
print(tuple(b))


f = [1, 3, '55', '666', 0]

for i in range(len(f)):
    print(i)

z = 'dfjk56nflk33fvm,lfv5p0097vktl66e'

# g = [int(i) for i in z if '0' <= i <= '9']
g = [int(i) for i in z if i.isdigit()]

print(g)
