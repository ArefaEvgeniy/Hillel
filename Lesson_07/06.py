from collections import namedtuple


Aircraft = namedtuple('Aircraft', 'product nember seats year code')
aircraft_1 = ['Boeing', 747, 416, 1998, 'AEW-344']
aircraft_2 = ['Boeing', 747, 416, 2001, 'BR-778']
aircraft_3 = ['AirBus', 445, 333, 2004, 'SRR-775']

aircrafts = [aircraft_1, aircraft_2, aircraft_3]
a_1 = Aircraft('Boeing', 747, 416, 1998, 'AEW-344')
a_2 = Aircraft('Boeing', 747, 416, 2001, 'BR-778')
a_3 = Aircraft('AirBus', 445, 333, 2004, 'SRR-775')

a_list = [a_1, a_2, a_3]

for aircraft in aircrafts:
    if aircraft[1] > 400:
        print(f'Aircraft {aircraft[-1]}')


print("-" * 50)
for aircraft in a_list:
    if aircraft.seats > 400:
        print(f'Aircraft {aircraft[-1]}')

print("-" * 50)
for aircraft in a_list:
    if aircraft[2] > 400:
        print(f'Aircraft {aircraft[-1]}')
