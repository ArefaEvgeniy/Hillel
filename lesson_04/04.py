import datetime


name = "Євген"
age = 44

now = datetime.datetime.now()
print("Мене звати %s. Мені %s роки. %s класно ім'я" % (name, age, name))
print(datetime.datetime.now() - now)
print('-' * 50)

now = datetime.datetime.now()
print("Мене звати {}. Мені {} роки. {} класно ім'я".format(name, age, name))
print(datetime.datetime.now() - now)
print('-' * 50)

now = datetime.datetime.now()
print(f"Мене звати {name}. Мені {age} роки. {name} класно ім'я")
print(datetime.datetime.now() - now)
print('-' * 50)
