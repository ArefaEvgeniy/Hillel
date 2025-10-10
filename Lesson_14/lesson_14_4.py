import json
import pickle


class Plane:

    def __init__(self, model, speed, range, sits):
        self.model = model
        self.speed = speed
        self.range = range
        self.sits = sits

    def __str__(self):
        return f"{self.model}"

    def display_info(self):
        print(f"Model: {self.model}, Sits: {self.sits}, "
              f"Speed: {self.speed} km/h, Range: {self.range} km")

    def order(self, name, kilometers):
        self.range += kilometers
        ...


class PlaneList(list):

    def __add__(self, other):
        if isinstance(other, PlaneList):
            new_list = PlaneList(self)
            for plane in other:
                if plane not in new_list:
                    new_list.append(plane)
            return new_list
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, PlaneList):
            new_list = PlaneList()
            for plane in self:
                if plane not in other:
                    new_list.append(plane)
            return new_list
        return NotImplemented

    def append(self, __object):
        if isinstance(__object, Plane) and __object not in self:
            super().append(__object)

    def __str__(self):
        return "PlaneList: [" + ", ".join(str(plane) for plane in self) + "]"


if __name__ == "__main__":
    plane_1 = Plane(model="Boeing 737", speed=850, range=5600, sits=180)
    plane_2 = Plane("Airbus A320", 830, 6100, 150)
    plane_3 = Plane("Embraer E190", 820, 4500, 100)
    plane_4 = Plane("Bombardier CRJ900", 820, 3700, 90)
    plane_5 = Plane("Sukhoi Superjet 100", 870, 4500, 98)
    plane_6 = Plane("Tupolev Tu-204", 870, 6200, 210)

    plane_list_1 = PlaneList([plane_1, plane_2, plane_3])
    plane_list_2 = PlaneList([plane_2, plane_5, plane_6, plane_1])
    print(plane_list_1)
    print(plane_list_2)

    plane_list_1.append(1)
    plane_list_1.append(plane_1)
    plane_list_1.append(plane_4)
    print(plane_list_1)

    plane_list_3 = plane_list_1 + plane_list_2
    print(plane_list_3)

    plane_list_4 = plane_list_1 - plane_list_2
    print(plane_list_4)

    json_data = []
    for plane in (plane_1, plane_2, plane_3, plane_4, plane_5, plane_6):
        json_data.append({
            "model": plane.model,
            "speed": plane.speed,
            "range": plane.range,
            "sits": plane.sits
        })

    with open("planes.json", "w") as file:
        json.dump(json_data, file)

    with open("planes.pkl", "wb") as file:
        pickle.dump((plane_1, plane_2, plane_3, plane_4, plane_5, plane_6), file)
