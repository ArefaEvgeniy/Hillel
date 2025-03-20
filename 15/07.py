from PlaneManager import PlaneManager


with PlaneManager('plane_1.pkl') as data:
    data[6].order('Dnipro-Tallin', 789)
    data[0].order('Dnipro-Tallin', 789)
    for plane in data:
        print(plane)

print('END')
