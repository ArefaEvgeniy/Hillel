age = input("Enter your age: ")

if not (age.isdigit()) or int(age) <= 0:
    print("a must be a positive")
elif int(age) < 10:
    print("Milk")
elif int(age) < 18:
    print("Coca-Cola")
elif int(age) < 30:
    print("Coffee")
elif int(age) < 100:
    print("Beer")
else:
    print("Invalid age")
