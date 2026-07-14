from abstract import SystemData


class Temperature(SystemData):
    def get_data(self):
        self.data = {}
        ...

    def prepare_data(self):
        ...

    def print_data(self):
        ...
