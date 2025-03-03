with open('Example.txt', 'r') as file:
    data_1 = file.read(5)
    print(data_1)
    data_2 = file.read(5)
    print(data_2)
    data_3 = file.read(10)
    print(data_3)

print('-' * 50)
with open('Example.txt', 'r') as file:
    data_1 = file.readline().strip()
    print(data_1)
    data_2 = file.readline().strip()
    print(data_2)
    data_3 = file.readline().strip()
    print(data_3)

print('-' * 50)
with open('Example.txt', 'r') as file:
    data = file.readlines()
    data_1 = file.read(4)

print(data)
print(f'data: "{data_1}"')
