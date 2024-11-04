# Перевірка того, що число є простим, за допомогою циклу
number = int(input("input positive number "))
i = 2
while i < number:
    if number % i == 0:
        # Якщо число ділиться без залишку на інше число, то це число не є простим
        print("It is not a prime number")
        break
    i = i + 1
else:  # виконається тільки якщо break в циклі не буде викликаний.
    print("It is a prime number")
