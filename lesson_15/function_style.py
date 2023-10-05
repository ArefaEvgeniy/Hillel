def get_cpu():
    ...


def get_memory():
    ...


def get_processors():
    ...


def get_temperatures():
    ...


def prepare_data(cpu, memory, pids, temperatures):
    def get_suffix(value):
        new_value = None
        ...
        return new_value

    data = None
    ...
    return data


def print_info(data):
    ...


def main():
    while True:
        cpu = get_cpu()
        memory = get_memory()
        pids = get_processors()
        temperatures = get_temperatures()
        data = prepare_data(cpu, memory, pids, temperatures)
        print_info(data)


if __name__ == '__main__':
    main()
