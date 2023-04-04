from dataclasses import dataclass

@dataclass
class Bill:
    table_number: int
    meal_amount: float
    served_by: str
    tip_amount: float = 0.0


bill_1 = Bill(table_number=5, meal_amount=50.5, served_by="John", tip_amount=7.5)

print(bill_1.__annotations__)
print(bill_1.__doc__)
print(bill_1.__repr__)
