z = None
try:
    a = [10, 45, 67]
    b = 10
    c = a[1] / b
    if c > 4:
        raise ValueError("Value exceeds 4")
    z = 1
except Exception as err:
    print(f"Error: {err}")
    c = -1


print(c)
print(z)
