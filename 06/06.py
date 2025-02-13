human = {"name": "Alexander",
        "lastname": "Glock",
        "age": 36,
        "address": {"street": "Lisova", "house": 87, "flat": 705}
}

house = human.get("address").get("house")
print(human.items())

for key, values in human.items():
    print(f"{key}: {values}")
