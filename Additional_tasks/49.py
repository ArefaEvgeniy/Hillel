# Написати клас Car в якому є 3 атрибути класу:
# - FUEL_TYPES (список), в якому знаходиться перелік доступних значень
# типів авто, наприклад: ['бензин', 'дизель', 'електрика', 'гібрид']
# - COLORS (порожній список) – в якому зберігаються всі унікальні значення
# кольорів створених за цим класом об'єктів
# - NUMBER_OF_CARS - кількість створених об'єктів.
# Конструктор приймає 4 обов'язкові аргументи: model, year, color, fuel_type.
# Перші 3 аргументи присвоюються 3-м атрибутам об'єкта. В атрибут fuel_type
# об'єкту присвоюється результат статичного методу is_valid_fuel_type() в
# який передається аргумент fuel_type та атрибут класу FUEL_TYPES. Даний
# метод перевіряє, чи є значення fuel_type у списку FUEL_TYPES. Якщо
# входить, це значення повертається статичним методом is_valid_fuel_type(),
# якщо ні, то повертається перше значення списку FUEL_TYPES.
# Також у конструкторі необхідно збільшити атрибут класу NUMBER_OF_CARS на
# одиницю, а також внести до атрибуту класу COLORS аргумент color, якщо таке
# значення в атрибуті класу COLORS відсутнє. Крім цього у об'єкта повинен
# з'явиться атрибут number, до якого буде записано значення якой за рахунком
# цей об'єкт був створений (грубо кажучи значення NUMBER_OF_CARS на момент
# створення об'єкта).
# Також необхідно передбачити, щоб під час друку об'єкта роздруковувалося
# б: "модель – рік_випуску – тип_двигуна - колір" .
# У класу повинен бути метод numbers який би поводився як атрибут. При
# його виклику car.numbers має видаватися, наприклад: "2 from 4". Тобто
# це другий автомобіль із 4-х вироблених.
# Крім цього у класі повинні бути ще 2 методи класу get_used_colors() та
# get_number_of_cars(). Перший з яких повертає кількість унікальних
# кольорів вироблених автомобілів, грубо кажучи довжину списку COLORS.
# Другий метод повертає кількість всього вироблених автомобілів.
# class Car:
#     FUEL_TYPES = ['бензин', 'дизель', 'електрика', 'гібрид']
#     COLORS = []
#     NUMBER_OF_CARS = 0
# ...
# car_1 = Car('Zaz', 1979, 'дизель', 'black')
# car_2 = Car('BMW', 2000, 'бензин', 'red')
# car_3 = Car('VOLVO', 2012, 'електрикаcccc', 'black')
# car_4 = Car('Mersedes', 2012, 'гібрид', 'black')
# print('COLORS:', Car.get_used_colors())
# print('NUMBER_OF_CARS:', Car.get_number_of_cars())
# for item in (car_1, car_2, car_3, car_4):
#     print('item:', item)
#     print('numbers:', item.numbers)


class Car:
    FUEL_TYPES = ['бензин', 'дизель', 'електрика', 'гібрид']
    COLORS = []
    NUMBER_OF_CARS = 0

    def __init__(self, model, year, fuel_type, color):
        self.model = model
        self.year = year
        self.color = color
        self.fuel_type = self.is_valid_fuel_type(fuel_type, Car.FUEL_TYPES)
        if color not in Car.COLORS:
            Car.COLORS.append(color)
        Car.NUMBER_OF_CARS += 1
        self.number = Car.NUMBER_OF_CARS

    def __str__(self):
        return f"{self.model} – {self.year} – {self.fuel_type} - {self.color}"

    @property
    def numbers(self):
        return f'{self.number} from {Car.NUMBER_OF_CARS}'

    @staticmethod
    def is_valid_fuel_type(fuel_type, fuel_types):
        res = None
        if fuel_type and fuel_types and isinstance(fuel_types, list):
            res = fuel_type if fuel_type in fuel_types else fuel_types[0]
        return res

    @classmethod
    def get_used_colors(cls):
        return len(cls.COLORS)

    @classmethod
    def get_number_of_cars(cls):
        return cls.NUMBER_OF_CARS


car_1 = Car('Zaz', 1979, 'дизель', 'black')
car_2 = Car('BMW', 2000, 'бензин', 'red')
car_3 = Car('VOLVO', 2012, 'електрикаcccc', 'black')
car_4 = Car('Mersedes', 2012, 'гібрид', 'black')

print('COLORS: ', Car.get_used_colors())  # -> 'COLORS: 2'
print('NUMBER_OF_CARS: ', Car.get_number_of_cars())  # -> 'NUMBER_OF_CARS: 4'
for item in (car_1, car_2, car_3, car_4):
    print('item:', item)
    print('numbers:', item.numbers)
