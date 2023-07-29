from dataclasses import dataclass


class BillGeneral:
    """FFF"""

    def __init__(self, table: int, mean_amount: float, served_by: str, tip_amount: float):
        self.table = table
        self.mean_amount = mean_amount
        self.served_by = served_by
        self.tip_amount = tip_amount


@dataclass
class Bill:
    table: int
    mean_amount: float
    served_by: str
    tip_amount: float = 0.0

    def get_table(self):
        return self.table


bill_0 = Bill(table=5, mean_amount=50.4, served_by='John', tip_amount=7.5)
bill_1 = BillGeneral(table=5, mean_amount=50.4, served_by='John', tip_amount=7.5)

print(Bill.__annotations__)
print(Bill.__doc__)
print(bill_1.__doc__)

print('-' * 50)

print(bill_0)
print(bill_0.get_table())
print(bill_1)
