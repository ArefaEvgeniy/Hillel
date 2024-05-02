from dataclasses import dataclass


@dataclass
class Bill:
    table_number: int
    meal_amount: float
    served_by: str
    sales: float


a_1 = Bill(table_number=5, meal_amount=56.12, served_by='Alex', sales=0.0)
a_2 = Bill(table_number=2, meal_amount=16.99, served_by='Alex', sales=5.3)
a_3 = Bill(table_number=3, meal_amount=120.00, served_by='Kite', sales=3.5)

print(a_1)
print(a_1.table_number)
print(a_1.meal_amount)
print(a_1.served_by)
print(a_1.__annotations__)

print('-' * 100)


class Bill2:

    def __init__(self, table_number: int, meal_amount: float, served_by: str, sales: float):
        self.table_number = table_number
        self.meal_amount = meal_amount
        self.served_by = served_by
        self.sales = sales

    def __str__(self):
        return (f'Bill2(table_number={self.table_number}, meal_amount={self.meal_amount}, '
                f'served_by=\'{self.served_by}\', sales={self.sales})')


b_1 = Bill2(table_number=5, meal_amount=56.12, served_by='Alex', sales=0.0)
print(b_1)
print(b_1.table_number)
print(b_1.meal_amount)
print(b_1.served_by)
# print(b_1.__annotations__)
