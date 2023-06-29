ss = "Меня зовут {}, мне {} года. {} красивое имя."
ss_1 = "Меня зовут {0}, мне {1} года. {0} красивое имя."
ss_2 = "Меня зовут {name}, мне {age} года. {name} красивое имя."

mm = 'Jon'
nn = '22'

print(ss.format(mm, nn, 'Tom'))
print(ss_1.format('Tom', mm, nn))
print(ss_2.format(age=nn, name=mm))

coord = (3, 5)
print('X:{0[0]}, Y:{0[1]}'.format(coord))

name = 'Jonson'

print('{:<30}'.format(name))
print('{:^30}'.format(name))
print('{:>30}'.format(name))

pi = 3.14159
print('{:.3}'.format(pi))
