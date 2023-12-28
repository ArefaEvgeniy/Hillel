class Bill:
    table_number: int
    meal_amount: float
    served_by: str
    tip_amount: float = 0.0

    def func_1(self):
        print(self.table_number)
        ...

    def __add__(self):
        ...

    @staticmethod
    def func_2():
        print('Hello')

    @classmethod
    def func_3(cls):
        print(cls.table_number)


a = Bill()
a.func_1()
a.func_2()
a.func_3()
