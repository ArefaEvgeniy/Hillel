print("START")
a = 10
b = 3
d = [1, 2, 3]

...

try:
    print("Before exception")
    c = a / b  # ZeroDivisionError: division by zero
    e = d[7]
    print(e)
    print(2 + '4')
    print("After exception")
# except (ZeroDivisionError, IndexError):
except ZeroDivisionError:
    print("Division by zero")
    c = 0
    e = None
except IndexError:
    print("Index error")
    e = 0
except LookupError:
    print("Lookup error")
    e = -1
except TypeError:
    print("Type error")
except Exception as err:
    print("Some exception")
    print(err)
    c = None
    e = None
else:
    print("No exceptions")
finally:
    print("Finally block")

print(c)
print(e)
print("END")
