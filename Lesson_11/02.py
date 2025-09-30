file = open("test.txt", "r", encoding="utf-8")
try:
    content = file.read()
    print(content)
finally:
    file.close()


with open("test.txt") as file:
    content = file.read()

print(content)
