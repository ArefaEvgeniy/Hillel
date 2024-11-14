a_1 = (3, 6, 99, '0', 'sfgr')

print(a_1[2])

plane_1 = ('Airobus', 234, 1999, 'AE4546')
plane_2 = ('Airobus', 125, 2015, 'ZXRTYG')
plane_3 = ('Boing', 256, 2012, 'AE5566')
plane_4 = ('Boing', 333, 2024, 'RT556T')

planes = [plane_1, plane_2, plane_3, plane_4]

print(plane_2[2])
print(plane_4[3])
print(plane_4[1])

print('-' * 100)
from collections import namedtuple

Plane = namedtuple('XXX', ['producer', 'sits', 'year', 'number'])
plane_11 = Plane(producer='Airobus', sits=234, year=1999, number='AE4546')
plane_12 = Plane(producer='Airobus', sits=125, year=2015, number='ZXRTYG')
plane_13 = Plane(producer='Boing', sits=256, year=2012, number='AE5566')
plane_14 = Plane(producer='Boing', sits=333, year=2024, number='RT556T')

print(plane_12[2])
print(plane_14[3])
print(plane_14[1])
print('-' * 100)
print(plane_12.year)
print(plane_14.number)
print(plane_14.sits)
