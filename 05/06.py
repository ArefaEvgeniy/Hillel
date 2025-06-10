
name = "Kolia"
name_2 = "Olia"
name_3 = "Aleksandr"
age = 23.556


print(f"My name is {name:^10}. I am is {age+1:.2f} years old. {name:>10} is great name.")
print(f"My name is {name_2:^10}. I am is {age+1:.2f} years old. {name_2:>10} is great name.")
print(f"My name is {name_3:^10}. I am is {age+1:.2f} years old. {name_3:>10} is great name.")

print(f"My name is {name if age < 30 else name_3}")

