z = None
try:
    a = [10, 45, 67]
    b = 0
    c = a[1] / b
    z = 1
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    c = 1000
except (IndexError, KeyError):
    print("Error: Index out of range.")
    c = 0
except LookupError:
    print("Error: LookupError")
    c = -100
except Exception as err:
    print(f"Error: {err}")
    c = -1
else:
    print("Division successful.")
finally:
    print("Finally block executed.")


print(c)
print(z)
