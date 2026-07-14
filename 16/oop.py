import time

from cpu import CPU
from memory import Memory
from processors import Processors
from temperature import Temperature


class App:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.processors = Processors()
        self.temperature = Temperature()

    def run(self):
        while True:
            for item in [self.cpu, self.memory, self.processors, self.temperature]:
                item.get_data()
                item.prepare_data()
                item.print_data()

            time.sleep(2)

            # self.cpu.get_data()
            # self.memory.get_data()
            # self.processors.get_data()
            #
            # self.cpu.prepare_data()
            # self.memory.prepare_data()
            # self.processors.prepare_data()
            #
            # self.cpu.print_data()
            # self.memory.print_data()
            # self.processors.print_data()


app = App()
app.run()
