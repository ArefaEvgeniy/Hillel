age = int(input("Enter your age: "))

if age <= 0:
    print("Age cannot be negative.")
elif age < 10:
    print("Drink milk")
elif age <= 18:
    print("Drink juice")
elif age < 21:
    print("Drink cofe")
elif age < 100:
    print("Drink whisky")
else:
    print("You are too old to drink.")
