text = "Це тестовий текст, який містить слово 'тест' кілька разів.\nСтрока 2.\nОстання строка"

# with open("test_2.txt", "wb") as file:
#     file.write(text.encode("utf-8"))

with open("test_2.txt", "w", encoding="utf-8") as file:
    file.write(text)

with open("test_2.txt", "rb") as file:
    content = file.read()

print(content)
print(content.decode("utf-8"))

with open("test_2.txt", "rb") as file:
    content = file.read(6)

print(content)
print(content.decode("utf-8"))
