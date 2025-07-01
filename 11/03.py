str_1 = "练习汉语口"
str_2 = "Test text"
str_3 = "Двільний текст"

# print(str_1.encode())

# with open("01.txt", "wb") as file:
#     file.write(str_1.encode())

with open("01.txt", "w", encoding="utf-16") as file:
    file.write(str_1)

with open("01.txt", encoding="utf-16") as file:
    text = file.read()
    print(text)

with open("01.txt", "rb") as file:
    text = file.read()
    print(text)
    print(text.decode(encoding="utf-16"))

with open("01.txt", encoding="utf-16") as file:
    text = file.read(2)
    print(text)

with open("01.txt", "rb") as file:
    text = file.read(8)
    print(text.decode(encoding="utf-16"))
