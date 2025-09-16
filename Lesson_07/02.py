my_list = [1, 2, 3, ['e', 'w', [88.5, 44.6], 'y'], 4, 5]

human = {"name": "Alexander",
        "lastname": "Glock",
        "age": 36,
        "address": {"street": {"part": ["Lisova", "main"]}, "house": 87, "flat": 705}
}

house = human["address"]["house"]
print(house)  # виведе: 87

# Міняємо значення для квартири
human["address"]["flat"] = 700
print(human["address"]["flat"])  # виведе: 700

print(my_list[3][2][-1])
print(human["address"]["street"]["part"][-1])
