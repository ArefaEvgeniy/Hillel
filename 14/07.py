import json
import pickle

from plane import Plane


with open('plane.json') as file:
    data = json.load(file)

planes = []
for index, item in enumerate(data):
    planes.append(Plane(item["number"], item["year"], item["sits"]))
    planes[index].flights = item["flights"]
    planes[index].kilometers = item["kilometers"]
    print(planes[index])


planes[0].order('Dnipro-New-York', 4300)
print(planes[0])
print(planes[0].flights)

print('=' * 100)
with open('plane_1.pkl', 'rb') as file:
    new_plane, new_plane_2 = pickle.load(file)

print(new_plane)
new_plane.order('Dnipro-New-York', 4300)
print(new_plane)
print(new_plane_2)
