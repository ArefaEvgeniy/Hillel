import json

from lesson_14_4 import Plane


with open("planes.json", "r") as file:
    data = json.load(file)

planes = [Plane(**plane_data) for plane_data in data]
# {'model': 'Boeing 737', 'speed': 850, 'range': 5600, 'sits': 180}  ->  model="Boeing 737", speed=850, range=5600, sits=180
# Plane(model="Boeing 737", speed=850, range=5600, sits=180)

# planes = [Plane(*plane_data.values()) for plane_data in data]
# Plane("Boeing 737", 850, 5600, 180)

for plane in planes:
    print(plane)

planes[0].display_info()
