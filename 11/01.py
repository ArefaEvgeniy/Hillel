from os import path


f = open("1.txt", "w")
f.write("Test text\n2.next line")
f.close()


try:
    f = open("2.txt", "w")
    f.write("Test text\n2.next line")
finally:
    f.close()

file_path = "temp"
file_name = "file.txt"
res = path.join("..", file_path, file_name)
print(res)

with open("3.txt", "w") as f:
    f.write("Test text\n2.next line")
