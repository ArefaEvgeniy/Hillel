import const
import staff


class Planes:
    def __init__(self, year, number, model, hours=0):
        self.year = year
        self.number = number
        self.model = model
        self.hours = hours
        self.status = const.STATUSES[0]
        self.raises = []
        self.crew = {
            'pilot': [None, None],
            'stuarts': [None, None, None, None],
            'repear': []
        }

    def add_crew(self, person):
        if (type(person) in (staff.Pilot, staff.Stuart)
                and self.status == const.STATUSES[0]
                and person.status == const.STATUSES[0]):
            if type(person) == staff.Pilot and None in self.crew['pilot']:
                self.crew['pilot'].remove(None)
                self.crew['pilot'].append(person)
                person.status = const.STATUSES[2]
                print(f'Added pilot {person.name}')
            elif type(person) == staff.Stuart and None in self.crew['stuarts']:
                self.crew['stuarts'].remove(None)
                self.crew['stuarts'].append(person)
                person.status = const.STATUSES[2]
                print(f'Added pilot {person.name}')
            else:
                print('Not availabel place')

        elif type(person) == staff.Repear and self.status == const.STATUSES[4]:
            self.crew['repear'].append(person)
            person.status = const.STATUSES[2]

    def add_raise(self, raise_name, hours):
        ...

    def change_status(self, status):
        ...

