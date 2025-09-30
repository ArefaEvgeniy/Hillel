with open("test_2.txt", "r", encoding="utf-8") as file:
    new_data = file.read()

print(new_data)


with open("test_2.txt", "r", encoding="utf-8") as file:
    data_1 = file.read(4)
    data_2 = file.read(6)
    data_3 = file.read(10)
    print(f"1: {data_1}")
    print(f"2: {data_2}")
    print(f"3: {data_3}")

print('-' * 20)
with open("test_2.txt", "rb") as file:
    data_1 = file.read(4)
    data_2 = file.read(6)
    data_3 = file.read(16)
    print(f"1: {data_1.decode('utf-8')}")
    print(f"2: {data_2.decode('utf-8')}")
    print(f"3: {data_3.decode('utf-8')}")

print('-' * 20)
with open("test_2.txt", "r", encoding="utf-8") as file:
    data = file.readlines()
    print(data)

print('-' * 20)
with open("test_2.txt", "r", encoding="utf-8") as file:
    data_1 = file.readline()
    data_2 = file.readline()
    data_3 = file.readline()
    print(data_1.strip())
    print(data_2.strip())
    print(data_3.strip())
