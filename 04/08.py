while True:
    input_number = input("Enter a number: ")
    if input_number.isdigit():
        n = int(input_number)
        break
    else:
        print("Invalid input. Please enter a valid number.")


a = 1

while a > 100:
    a *= n
    n -= 1
else:
    print("Factorial calculation is complete.")
