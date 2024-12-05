import time


class General:
    def prepare(self):
        ...

    def print_data(self):
        ...


class CPU(General):
    def get(self):
        ...


class Memory(General):
    def get(self):
        ...

    def prepare(self):
        ...


class Processes(General):
    def get(self):
        ...

    def print_data(self):
        ...


class Main:
    def __init__(self, *args):
        self.data = args

    def run(self):
        while True:
            for item in self.data:
                item.get()
                item.prepare()
                item.print_data()
            time.sleep(2)


cpu = CPU()
memory = Memory()
processes = Processes()

main = Main(cpu, memory, processes)
main.run()
