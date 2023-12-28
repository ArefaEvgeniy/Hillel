from dataclasses import dataclass


@dataclass
class Bill:
    table_number: int
    meal_amount: float
    served_by: str
    tip_amount: float = 0.0


class Bill_2:
    def __init__(self, table_number: int, meal_amount: float, served_by: str, tip_amount: float = 0.0):
        self.table_number = table_number
        self.meal_amount = meal_amount
        self.served_by = served_by
        self.tip_amount = tip_amount
        self.float = float

    def __str__(self):
        return (f"Bill_2(table_number:{self.table_number}, meal_amount:{self.meal_amount}, served_by:{self.served_by}, "
                f"tip_amount:{self.tip_amount})")


bill_1 = Bill(4, 112.4, 'Ket', 0.0)
print(bill_1.meal_amount)
print(bill_1)
bill_2 = Bill_2(4, 112.4, 'Ket', 0.0)
print(bill_2.meal_amount)
print(bill_2)
