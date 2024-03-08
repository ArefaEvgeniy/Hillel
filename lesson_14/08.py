from dataclasses import dataclass


@dataclass
class Bill:
    table_number: int
    meal_amount: float
    served_by: str
    sale: int

    def get_sale(self):
        return self.sale


b_1 = Bill(12, 123.23, 'Ivan', 0)
b_2 = Bill(11, 0.65, 'Ivan', 2)
b_3 = Bill(1, 1123.00, 'Ivan', 10)

print(b_1)
print(b_2)
print(Bill.__annotations__)


class Bill2:

    def __init__(self, table_number: int, meal_amount: float, served_by: str, sale: int):
        self.table_number = table_number
        self.meal_amount = meal_amount
        self.served_by = served_by
        self.sale = sale

    def __str__(self):
        return (f"Bill(table_number={self.table_number}, meal_amount={self.meal_amount}, "
                f"served_by='{self.served_by}', sale={self.sale})")


b_4 = Bill2(12, 123.23, 'Ivan', 0)
print(b_4.__dict__)
print(b_4)
