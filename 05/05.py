string = "My name is {}. I am is {} years old. {} is great name."
string_2 = "My name is {0}. I am is {1} years old. {0} is great name."
string_3 = "My name is {name}. I am is {age} years old. {name} is great name."

name = "Kolia"
age = 33

print(string)
print(string.format("Kolia", 55, name, "Olia"))
print(string_2.format(name, 55, "Olia"))
print(string_3.format(age=age, name="Kolia"))
