from collections import defaultdict


defdict = defaultdict(lambda: 1)
#тепер при додаванні будь-якого ключа до словника, значення цього ключа буде порожній список

# Отримуємо значення за відсутнім ключем
print(defdict["d"])  # виведе: []
print(defdict["c"])
print(defdict["a"])

print(defdict)
