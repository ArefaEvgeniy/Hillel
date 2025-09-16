d = {'IBM': 125, 'ACME': 50, 'PHP': 40}


print("IBM" in d)  # виведе: True
print("Iva" in d)  # виведе: False
print(125 in d.values())  # виведе: True

for key in d:
    if 125 == d[key]:
        print(True)
