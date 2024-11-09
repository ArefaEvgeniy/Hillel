name = "Alice"
age = 25
height = 1.68

# Використовуємо плейсхолдери %s для рядків, %d для цілих чисел і %f для дробних чисел
s = "%s is %d years old and %f meters tall"
s_2 = "%s(name) is %s(age) years old and %s(height) meters tall. My name is %s(name)"

print(s % (name, age, height))

print(s % ('Bob', 34, 2.05))

print(s_2 % {name: 'Bob', age: age, height: 1.22})
