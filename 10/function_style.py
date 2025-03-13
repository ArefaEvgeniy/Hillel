def get_data():
    def get_CPU(data):
        ...
        return data

    def get_momory(data):
        ...
        return data

    def get_processes(data):
        ...
        return data

    def get_temperature(data):
        ...
        return data

    data = {}
    data = get_CPU(data)
    data = get_momory(data)
    data = get_processes(data)
    data = get_temperature(data)

    return data


def prepare_data(data):
    new_data = []
    ...
    return new_data


def print_data(data):
    ...


def main():
    while True:
        data = get_data()
        new_data = prepare_data(data)
        print_data(new_data)


main()
