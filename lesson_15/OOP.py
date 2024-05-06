import time


class Abstract:
    def prepare_data(self):
        pass

    def print_data(self):
        pass


class CPU(Abstract):
    def get_data(self):
        pass


class RAM(Abstract):
    def get_data(self):
        pass

    def print_data(self):
        pass


class Processes(Abstract):
    def get_data(self):
        pass

    def prepare_data(self):
        pass


class Fun(Abstract):
    def get_data(self):
        pass

    def prepare_data(self):
        pass

    def print_data(self):
        pass


def main():
    info = (CPU(), RAM(), Processes(), Fun())
    while True:
        for item in info:
            item.get_data()
            item.prepare_data()
            item.print_data()
        time.sleep(2)


if __name__ == '__main__':
    main()
