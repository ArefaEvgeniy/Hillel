print("START")
a = 10
b = 0

print("GO")
try:
    res = ((a + 4) * 5) / b
    print("CONTINUE")
    c = True if res else False
# except (ZeroDivisionError, TypeError, IndexError):
#     print("EXCEPTION ZeroDivisionError")
#     res = 0
except ZeroDivisionError:
    print("EXCEPTION ZeroDivisionError")
    res = 0
except TypeError:
    print("EXCEPTION TypeError")
    res = None
except IndexError:
    print("EXCEPTION IndexError")
    res = "!!!"
except LookupError:
    print("EXCEPTION LookupError")
    res = False
except Exception as err:
    print("EXCEPTION")
    print(err)
    res = False
else:
    print("ELSE")
finally:
    print("FINALLY")

print("res:", res)
print("END")


# if a > 1000:
#     ...
# elif a > 10:
#     ...
# elif a > 0:
#     ...