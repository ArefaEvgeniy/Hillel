import datetime
from dateutil.relativedelta import relativedelta
from dateutil import parser


class Person(object):
    PERSONS = []

    @staticmethod
    def parse_date(date):
        return parser.parse(date).date()

    @staticmethod
    def string_date(date):
        if date is not None:
            year = str(date.year)
            month = str(date.month).rjust(2, '0')
            day = str(date.day).rjust(2, '0')
            return '.'.join([day, month, year])
        else:
            return None

    def __init__(self, first_name, birth_date, gender, second_name=None, last_name=None, death_date=None):
        self.first_name = first_name.strip().title()
        self.birth_date = birth_date
        self.gender = gender
        self.second_name = second_name.strip().title() if second_name is not None else None
        self.last_name = last_name.strip().title() if last_name is not None else None
        self.death_date = death_date
        Person.PERSONS.append((self.last_name, self.first_name, self.second_name, self.string_date(self.birth_date),
                               self.string_date(self.death_date), self.gender, self.age, self.full_name))

    @property
    def age(self):
        if self.death_date:
            return relativedelta(self.death_date, self.birth_date).years
        else:
            return relativedelta(datetime.date.today(), self.birth_date).years

    @property
    def full_name(self):
        full_name = ''
        for item in (self.last_name, self.first_name, self.second_name):
            if item is not None:
                full_name += f' {item}'
        return full_name

    @classmethod
    def search_person(cls, search_key):
        result = []
        if search_key == '*':
            for item in cls.PERSONS:
                result.append(cls.build_search_result_line(item))
        else:
            for item in cls.PERSONS:
                full_name = item[7]
                if search_key.lower() in full_name.lower():
                    result.append(cls.build_search_result_line(item))
        return result

    @staticmethod
    def build_search_result_line(data):
        full_name = data[7]
        age_expl = 'років'
        if data[6] % 10 == 1:
            age_expl = 'рік'
        if data[6] % 10 in (2, 3, 4):
            age_expl = 'роки'
        if data[6] % 100 in (11, 12, 13, 14):
            age_expl = 'років'
        age = f'{data[6]} {age_expl},'
        gender = f'{data[5]}.'
        birth_expl = 'Народився' if data[5] == 'чоловік' else 'Народилася'
        birth_date = f'{birth_expl} {data[3]}.'
        death_date = ''
        if data[4]:
            death_expl = 'Вмер' if data[5] == 'чоловік' else 'Вмерла'
            death_date = f' {death_expl} {data[4]}'
        return ' '.join((full_name, age, gender, birth_date, death_date))
