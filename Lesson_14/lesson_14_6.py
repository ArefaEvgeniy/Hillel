import pickle

from lesson_14_4 import Plane


with open("planes.pkl", "rb") as file:
    planes = pickle.load(file)

for plane in planes:
    print(plane)

planes[0].display_info()
