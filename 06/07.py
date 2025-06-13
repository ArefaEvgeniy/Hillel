from collections import defaultdict
defdict = defaultdict(list)
#тепер при додаванні будь-якого ключа до словника, значення цього ключа буде порожній список

# Отримуємо значення за відсутнім ключем
print(defdict["d"]) # виведе: []

# Оскільки ми знаємо, що за будь-яким ключем буде список, ми можемо використовувати методи властиві спискам
for i in range(5):
    defdict[i].append(i * 5)

print(defdict) # виведе: defaultdict(<class 'list'>, {0: [0], 1: [5], 2: [10], 3: [15], 4: [20]})
# Створюємо defaultdict, який повертає 0 для будь-якого ключа
dct = defaultdict(lambda: 0)
print(dct["d"]) # виведе: 0
