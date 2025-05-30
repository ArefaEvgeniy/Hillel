age = input("Enter your age: ")

if not age.isdigit() or int(age) == 0:
    print("Wrong value")
elif int(age) <= 10:
    print("1")
elif int(age) < 20:
    print("2")
elif int(age) < 30:
    print("3")
elif int(age) < 50:
    print("4")
else:
    print("You are very old")
