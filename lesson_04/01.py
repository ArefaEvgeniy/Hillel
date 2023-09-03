template_1 = "Мене звати %s. Мені %s роки. %s класно ім'я"
name = "Євген"
age = 44

# template_1 = "Мене звати %s. Мені %s роки. %s класно ім'я" % (name, age, name)
print(template_1 % (name, age, name))
print("Мене звати %(name)s. Мені %(age)s роки. %(name)s класно ім'я" % {"name": name, "age": age})
