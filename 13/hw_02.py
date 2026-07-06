# Створіть клас для опису товару (припустимо, це заділ для інтернет-магазину).
# Як поля товару можете використовувати значення ціни, опис, габарити товару.
# Створіть пару екземплярів вашого класу та протестуйте їхню роботу. Створіть
# клас "Покупець". Як поля можна використовувати прізвище, ім'я, по батькові,
# мобільний телефон і т.д. Створіть клас "Замовлення". Замовлення може містити
# кілька товарів, причому кількість кожного з товарів може бути різною.
# Замовлення має бути "підв'язане" до користувача, який його здійснив.
# Реалізуйте метод обчислення сумарної вартості замовлення. Визначте метод
# str() для коректного виведення інформації про це замовлення.
#
# class Item:
#
#     def __init__(self, name, price, description, dimensions):
#         self.price = price
#         self.description = description
#         self.dimensions = dimensions
#         self.name = name
#
#     def __str__(self):
#         pass
#
# class User:
#
#     def __init__(self, name, surname, numberphone):
#         self.name = name
#         self.surname = surname
#         self.numberphone = numberphone
#
#     def __str__(self):
#         pass
#
# class Purchase:
#     def __init__(self, user):
#         self.products = {}
#         self.user = user
#         self.total = 0
#
#     def add_item(self, item, cnt):
#         self.products[item] = cnt
#
#     def __str__(self):
#         pass
#
#     def get_total(self):
#         pass
#
# lemon = Item('lemon', 5, "yellow", "small", )
# apple = Item('apple', 2, "red", "middle", )
# print(lemon)  # lemon, price: 5
#
# buyer = User("Ivan", "Ivanov", "02628162")
# print(buyer)  # Ivan Ivanov
#
# cart = Purchase(buyer)
# cart.add_item(lemon, 4)
# cart.add_item(apple, 20)
# print(cart)
# """
# User: Ivan Ivanov
# Items:
# lemon: 4 pcs.
# apple: 20 pcs.
# """
# assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
# assert cart.get_total() == 60, "Всього 60"
# assert cart.get_total() == 60, 'Повинно залишатися 60!'
# cart.add_item(apple, 10)
# print(cart)
# """
# User: Ivan Ivanov
# Items:
# lemon: 4 pcs.
# apple: 10 pcs.
# """
#
# assert cart.get_total() == 40
