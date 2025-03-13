class General:
    def prepare_data(self):
        ...

    def print_data(self):
        ...


class CPU(General):
    def get_data(self):
        ...

    def prepare_data(self):
        ...


class Memory(General):
    def get_data(self):
        ...


class Process(General):
    def get_data(self):
        ...

    def prepare_data(self):
        ...

    def print_data(self):
        ...


class Temperature(General):
    def get_data(self):
        ...

    def prepare_data(self):
        ...

    def print_data(self):
        ...


class Main:
    def __init__(self, *args):
        self.data = args

    def start(self):
        while True:
            for item in self.data:
                item.get_data()
                item.prepare_data()
                item.print_data()


main = Main(CPU(), Memory(), Process(), Temperature())
main.start()
