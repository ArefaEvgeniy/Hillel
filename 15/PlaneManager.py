import pickle


class PlaneManager:
    def __init__(self, filename):
        self.filename = filename
        self.data = []

    def __enter__(self):
        file = open(self.filename, 'rb')
        self.data = pickle.load(file)
        for plane in self.data:
            if plane.kilometers > 0:
                plane.kilometers += 10
        file.close()
        return self.data

    def __exit__(self, exc_type, exc_value, traceback):
        file = open(self.filename, 'wb')
        pickle.dump(self.data, file)
        file.close()
        if exc_type:
            print(f"Error: {exc_type}, {exc_value}")
        return False
