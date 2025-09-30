data = "Hello world!\nПривіт".encode()
print(data)

with open("test_2.txt", "wb") as file:
    file.write(data)

print('-' * 20)
with open("test_2.txt", "r", encoding="utf-8") as file:
    new_data = file.read()

print(new_data)

print('-' * 20)
with open("test_2.txt", "rb") as file:
    new_data_2 = file.read()

print(new_data_2.decode('utf-8'))
