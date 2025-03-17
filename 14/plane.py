class Plane:

    def __init__(self, number: str, year: int, sits: int):
        self.number = number
        self.year = year
        self.sits = sits
        self.flights = 0
        self.kilometers = 0

    def __str__(self):
        return f"Number: {self.number}, {self.year}, sits: {self.sits}, {self.kilometers} km"

    def order(self, name: str, kilometers: int):
        self.flights += 1
        self.kilometers += kilometers
        ...
