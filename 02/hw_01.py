# 1. Квадрат числа.
# Користувач вводить число. Програма виводить його квадрат.
# Приклад:
# Введіть число: 5
# Квадрат числа: 25
#
# 2. “Середнє трьох чисел”
# Програма запитує три числа і виводить їх середнє арифметичне.
# Приклад:
# Введіть три числа: 2, 4, 6
# Середнє: 4.0
#
# 3. “Перетворення хвилин у години”
# Користувач вводить кількість хвилин. Програма виводить, скільки це годин і хвилин.
# Приклад:
# Введіть кількість хвилин: 135
# 2 години 15 хвилин
#
# 4. “Розрахунок знижки”
# Користувач вводить ціну товару і розмір знижки у %.
# Програма виводить кінцеву ціну.
# Приклад:
# Введіть ціну: 1000
# Введіть знижку (%): 15
# Ціна зі знижкою: 850.0
#
# 5. “Остання цифра числа”
# Користувач вводить ціле число, програма виводить його останню цифру.
# Приклад:
# Введіть число: 347
# Остання цифра: 7
#
# 6. “Периметр прямокутника”
# Користувач вводить довжину і ширину. Програма виводить периметр.
# Приклад:
# Введіть довжину: 5
# Введіть ширину: 3
# Периметр: 16
#
# 7. Виведення числа в стовпчик
# Написати програму, яка просить користувача ввести 4-х значне число з клавіатури, після чого друкує
# на екрані стовпчик цифр, з якого це число складається. Наприклад, користувач вводить 1234, а програма виводить:
# 1
# 2
# 3
# 4
# Завдання необхідно вирішити, використовуючи методи поділу (підказка // і % або divmod).
# Виведення в стовпчик можна зробити за допомогою 4-х функцій print.
# Користувач може ввести будь-яке 4 значне ціле число. Будь-яке 4-х значне число - це число, яке складається
# з 4-х цифр, де кожна цифра може бути від 0 до 9 включно.
# Ваше рішення має це враховувати! Якщо користувач ввів не ціле число, це проблема користувача, а не вашої програми.
#
# Створюйте рішення, виходячи з того, що число ЗАВЖДИ 4-х значне.

# Task №1
user_number = int(input("Enter a number: "))
print("Squared number: ", user_number ** 2)

# Task №2
first_user_number = int(input("Enter the first number: "))
second_user_number = int(input("Enter the second number: "))
third_user_number = int(input("Enter the third number: "))
print("Average number: ", (first_user_number + second_user_number + third_user_number) / 3)

# Task №3
minutes = int(input("Enter amount of minutes: "))
print(minutes, "minutes, it's:", (minutes // 60), "hours", (minutes % 60), "minutes")

# Task №4
user_price = int(input("Enter price: "))
user_discount = int(input("Enter discount rate (%): "))
print("Price, including discount: ", user_price * (1 - user_discount / 100))

#Task №5
user_whole_number = int(input("Enter a whole number: "))
print("Last number: ", user_whole_number % 10)

# Task №6
user_width = int(input('Enter width: '))
user_length = int(input('Enter length: '))
print("Perimeter: ", (user_width + user_length) * 2)

# Task №7
user_4_digit_number = int(input("Enter four-digit number: "))
print(user_4_digit_number // 1000)
print((user_4_digit_number // 100) % 10)
print((user_4_digit_number // 10) % 10)
print((user_4_digit_number // 1) % 10)
