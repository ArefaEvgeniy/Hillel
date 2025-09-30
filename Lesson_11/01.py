file = open("test.txt", "w", encoding="utf-8")
file.write("Привіт всесвіт!")
file.close()


file = open("test.txt", "r", encoding="utf-8")
content = file.read()
print(content)
file.close()
