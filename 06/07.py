d2 = {"A1": "123", "A2": "456"}
d3 = d2.copy()
d4 = {}
d4.update(d2)

d2["A1"] = 100
print(d3)

student = {"name": "Alexander", "lastname": "Tsin", "age": 36, "group": "PN121"}

a = student.pop("lastname")

print(student)
print(a)
