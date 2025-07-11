import time


class Maksim:
    def prepare_data(self):
        ...

    def print_data(self):
        ...


class CPU(Maksim):
    def get_data(self):
        ...


class Memory(Maksim):
    def get_data(self):
        ...


class Process(Maksim):
    def get_data(self):
        ...

    def prepare_data(self):
        ...


class App:
    def __init__(self, *args):
        self.items = args

    def start(self):
        while True:
            for item in self.items:
                item.get_data()
                item.prepare_data()
                item.print_data()

            time.sleep(3)


app = App(CPU(), Memory(), Process())
app.start()
