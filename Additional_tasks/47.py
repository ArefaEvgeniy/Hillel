# Написати програму яка складається з вічного циклу, що очікує введення числа
# або одне із значень: "вихід", "exit", "quit", "e" або "q" у будь-якому
# регістрі. При введенні одного з цих значень відбувається вихід із вічного
# циклу. При будь-якому іншому введенні викликається окрема функція, яка вміє
# розпізнавати введені числа. Сама функція нічого не роздруковує, вона
# повертає рядок типу: "Ви ввели негативне дробове число: -6.7" або "Ви ввели
# не коректне число: Erdf"
# Потім у циклі виводиться це повідомлення і цикл починається знову чекаючи
# наступного введення. Функція на вхід приймає рядок із введення з вічного
# циклу. Аналізує її виключно методом .isdigit() та іншими методами рядків,
# без доп.бібліотек і переводить рядок у число, якщо це можливо.
# Функція вміє розпізнавати негативні числа та десяткові дроби, а також
# розпізнає десяткові дроби як з точкою, так і з комою.
# Функція повертає рядок в якому описується яке число введено - негативне або
# позитивно, ціле або дробове і виводить його або повідомляє, що введено не
# коректне число.
#
# *Додатково: правильно розпізнається десятковий дріб без першого нуля.
# Крім того функція вміє розпознавати нуль.
#
# Приклади:
# -6,7    → Ви ввели від'ємне дробове число: -6.7
# 5       → Ви ввели позитивне ціле число: 5
# 5.4r    → Ви ввели неправильне число: 5.4r
# -.777   → Ви ввели від'ємне дробове число: -0.777
# ,45     → Ви ввели позитивне дробове число: 0.45
# 0       → Ви ввели нуль
# 0,00    → Ви ввели нуль
# -0.45.6 → Ви ввели не правильне число: -0.45.6
# -5-6    → Ви ввели не правильне число: -5-6
# .-777   → Ви ввели не правильне число: .-777