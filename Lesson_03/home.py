numberOne = float(input("Enter first number "))
numberTwo = float(input("Enter second number "))
operation = input("Choose Operation: + as addition, - as subtraction, * as multiplication, / as divide: ")
result = None

# if operation in ["+", "-", "*", "/"]:
# if operation == "+" or operation == "-" or operation == "*" or operation == "/":
if operation == "+":
    result = numberOne + numberTwo

elif operation == "-":
    result = numberOne - numberTwo

elif operation == "*":
    result = numberOne * numberTwo

elif operation == "/":
    if numberTwo == 0:
        print("Error: can't be divided by zero")
    else:
        result = numberOne / numberTwo
else:
    print("Calculator doesn't work with another operations")

if result is not None:
    print(numberOne, operation, numberTwo, "=", result)
