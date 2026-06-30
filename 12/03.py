file = open("test.txt", "r")
try:
    content = file.read()
finally:
    file.close()


file_2 = open("test.txt", "r")
data_1 = file_2.read(9)
data_2 = file_2.read(10)
data_3 = file_2.read(3)
file_2.close()
print(data_1)
print("--------------------")
print(data_2)
print("--------------------")
print(data_3)

with open("test.txt", "r") as file_3:
    data_lines = file_3.readlines()

print("--------------------")
print(data_lines)

with open("test.txt", "r") as file_3:
    data_line_1 = file_3.readline().strip()
    data_line_2 = file_3.readline().strip()
    data_line_3 = file_3.readline().strip()

print("--------------------")
print(data_line_1)
print("--------------------")
print(data_line_2)
print("--------------------")
print(data_line_3)
