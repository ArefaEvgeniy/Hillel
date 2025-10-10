import json

from lesson_14_4 import Plane


with open("planes.json", "r") as file:
    data = json.load(file)

planes = [Plane(**plane_data) for plane_data in data]
for plane in planes:
    print(plane)

planes[0].display_info()
