# Створити 2 класу truck та car, які є спадкоємцями класу auto з попереднього
# домашнього завдання.
# Об'єкти класу truck мають додатковий обов'язковий атрибут max_load.
# Перевизначений метод move перед появою напису «move» виводить
# напис «attention», його реалізацію зробити з допомогою оператора super.
# А також додатковий метод load. При його виклику відбувається пауза 1 сек.
# потім видається повідомлення «load» і знову пауза 1 сек.
# Об'єкти класу car мають додатковий обов'язковий атрибут max_speed та при
# виклик методу move, після появи напису «move» має з'явитися напис
# "max speed is <max_speed>". Замість <max_speed> має виводиться значення
# обов'язкового атрибуму max_speed. Створити по 2 об'єкти для кожного з класів
# truck та car, перевірити всі їх методи та атрибути.
# При цьому об'єкти Truck і Car при створенні можуть приймати такі самі аргументи,
# що об'єкти класу Auto (brand, mark, age - обов'язкові, а color і weight -
# не обов'язкові).


import time
from home_1 import Auto


class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print("attention")
        super().move()

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"max speed is {self.max_speed}")
