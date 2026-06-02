while True:
    input_number = input("Enter a number: ")
    if input_number.isdigit():
        n = int(input_number)
        break
    else:
        print("Invalid input. Please enter a valid number.")
