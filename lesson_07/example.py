def save_data(config, data):
    ...


def process(data):
    result = None
    ...
    return result


def open_file():
    result = None
    ...
    return result


def load_data(config):
    result = None
    data = open_file()
    ...
    return result


def load_config():
    def get_valid(data):
        ...

    result = None
    data = open_file()
    get_valid(data)
    ...
    return result


def main():
    config = load_config()
    data = load_data(config)
    new_data = process(data)
    save_data(config, new_data)


main()
