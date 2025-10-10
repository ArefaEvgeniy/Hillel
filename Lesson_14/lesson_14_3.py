file = open("test.txt", "r")
data = file.read()
file.close()


with open("test.txt", "r") as file:
    data_2 = file.read()


def __enter__():
    print("Enter")

def __exit__():
    print("Exit")

