import time


class Abstract:

    def process_data(self):
        ...

    def print_data(self):
        ...


class CPU(Abstract):

    def get_data(self):
        ...


class Memory(Abstract):

    def get_data(self):
        ...

    def process_data(self):
        ...


class Process(Abstract):

    def get_data(self):
        ...

    def print_data(self):
        ...


class Temp(Abstract):

    def get_data(self):
        ...

    def process_data(self):
        ...

    def print_data(self):
        ...


class App:

    def __init__(self, *args):
        self.modules = [*args]

    def run(self):
        while True:
            for module in self.modules:
                module.get_data()
                module.process_data()
                module.print_data()

            time.sleep(2)


my_app = App(CPU(), Memory(), Process(), Temp())
my_app.run()
