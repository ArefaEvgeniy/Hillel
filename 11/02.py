with open("1.txt") as file:
    res = file.read()

print(res)

with open("1.txt") as file:
    res = file.read(4)
    print(res)
    res = file.read(7)
    print(res)

with open("1.txt") as file:
    res = file.readlines()

print(res)

with open("1.txt") as file:
    res = file.readline().strip()
    print(res)
    res = file.readline().strip()
    print(res)
    res = file.readline().strip()
    print(res)
