from dataclasses import dataclass


@dataclass
class Bill:
    table_number: int
    mael_amout: float
    served_by: str
    tip_amout: float = 0.0

    def my_method(self):
        print('My Method')
        print(self.mael_amout - self.mael_amout * self.tip_amout / 100)


bill_1 = Bill(table_number=3, mael_amout=50.5, served_by='Jack', tip_amout=5)

print(bill_1.table_number)
print(bill_1.mael_amout)
print(bill_1.served_by)
print(bill_1.tip_amout)
bill_1.my_method()

print(bill_1.__annotations__)
print('-' * 50)
print(bill_1)
