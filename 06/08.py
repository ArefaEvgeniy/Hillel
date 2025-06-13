from collections import namedtuple


Plane = namedtuple('Plane', 'fabric number sits year')

plane_1 = Plane('Airobus', 'FR-55534', 100, 1990)
plane_2 = Plane('Airobus', 'AA-0054', 250, 2000)
plane_3 = Plane('Boing', 'RT-ZZ56', 130, 2010)
plane_4 = Plane('Boing', 'EE-W334', 333, 2012)

planes = [plane_1, plane_2, plane_3, plane_4]

for plane in planes:
    if plane.sits > 200:
        print(f'{plane.number}, {plane.sits}')
