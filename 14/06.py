import json
import pickle

from plane import Plane


obj_1 = Plane('AE-4456', 2000, 58)
obj_2 = Plane('ZX-8080', 1981, 320)
obj_3 = Plane('YTR-45', 2025, 200)

obj_1.order('Dnipro-Drezden', 2198)
obj_1.order('Drezden-Riga', 1134)

obj_2.order('Dnipro-Kyiv', 453)
obj_2.order('Odessa-Krakiv', 1010)
obj_2.order('Dnipro-Bern', 2004)

print(obj_1)
print(obj_2)
print(obj_3)

data = []
for item in (obj_1, obj_2, obj_3):
    plane = {}
    plane.update({"number": item.number})
    plane.update({"year": item.year})
    plane.update({"sits": item.sits})
    plane.update({"flights": item.flights})
    plane.update({"kilometers": item.kilometers})
    data.append(plane)

with open('plane.json', 'w') as file:
    json.dump(data, file)


with open('plane_1.pkl', 'wb') as file:
    pickle.dump([obj_2, obj_3], file)
