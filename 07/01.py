flight_1 = ('Airobass', 'AE-7765RT', 2007, 220)
flight_2 = ('Airobass', 'RT-77XXT', 2010, 330)
flight_3 = ('Boing', 'XXTT5RT', 2000, 165)
flight_4 = ('Boing', 'YU7TY55RT', 2010, 312)

park = [flight_1, flight_2, flight_3, flight_4]

for item in park:
    if item[2] >= 300:
        print(item[1])


print('-' * 60)
from collections import namedtuple


Flight = namedtuple('Flight', ['fubric', 'number', 'year', 'sits'])
flight_5 = Flight(fubric='Airobass', number='AE-7765RT', year=2007, sits=220)
flight_6 = Flight(fubric='Airobass', number='RT-77XXT', year=2010, sits=330)
flight_7 = Flight(fubric='Boing', number='XXTT5RT', year=2000, sits=165)
flight_8 = Flight(fubric='Boing', number='YU7TY55RT', year=2010, sits=312)

park = [flight_5, flight_6, flight_7, flight_8]

for item in park:
    if item.sits >= 300:
        print(item.number)
