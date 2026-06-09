name = "Alice"
age = 25
height = 1.68567

print(f"{name[:8]:<8} is {age} years old and {height:.2f} meters tall. {name} - it is a name.")

name = "Bob"
print(f"{name[:8]:>8} is {age:x} years old and {height:.2f} meters tall. {name} - it is a name.")

name = "William II"
print(f"{name[:8]:^8} is {age:b} years old and {height:.2f} meters tall. {name} - it is a name.")
