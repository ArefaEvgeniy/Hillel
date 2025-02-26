# На запит від програми, користувач вводить 5-ти значне ціле, позитивне число.
# Вам необхідно "перевернути" цє число задом наперед, тобто щоб у результаті
# вийшло теж 5-ти значне число, але із зворотною послідовністю цифр.
# Вам не потрібно перевіряти, що користувач ввів правильне число - зробіть
# вигляд, що користувач завжди вводить 5 значне число. Тобто введене
# користувачем число завжди складатиметься з 5 цифр.
# Якщо користувач ввів інше число, це проблема користувача, а не вашої
# програми. Використовуються лише цілі числа. Для розв'язання задачі потрібно
# використовувати лише той зріз даних, який було пройдено.
# Тобто використовувати строки не можна.

# Приклади:
# Користувач ввів: 12345 - на екрані відображається: 54321
# Користувач ввів: 37568 - на екран відображається: 86573


# запитуємо у користувача 5-ти значне число
number = int(input("Enter a 5-digit number: "))

# перша цифра
tens_of_thousands = number // 10000

# друга цифра
thousands = (number // 1000) % 10

# третя цифра
hundreds = (number // 100) % 10

# четверта цифра
tens = (number // 10) % 10

# п'ята цифра
units = number % 10

# формуємо нове число,що складається з цифр у зворотному порядку
flipped_number = (units * 10000) + (tens * 1000) + (hundreds * 100) + (thousands * 10) + tens_of_thousands

# виводимо перевернуте число
print(flipped_number)

