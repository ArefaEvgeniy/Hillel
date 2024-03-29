import unittest

from person import Person


class TestPerson(unittest.TestCase):

    def setUp(self):
        self.person_1 = Person('Иван', 'Петров', 'Сидорович', '20.11.1980', '', 'm')
        self.person_1.valid()
        self.person_2 = Person('Tom', 'Black', '', '3.5.2010', '', 'm')
        self.person_2.valid()
        self.person_3 = Person('Natali', 'Kid', '', '15.9.1974', '14.9.1999', 'f')
        self.person_3.valid()

    def test_str(self):
        self.assertEqual(self.person_1.__str__(),
                         'Иван Петров Сидорович 43 роки, чоловік. Народився: 20.11.1980.')
        self.person_1.sex = 'f'
        self.assertEqual(self.person_1.__str__(),
                         'Иван Петров Сидорович 43 роки, жінка. Народилась: 20.11.1980.')
        self.assertEqual(self.person_2.__str__(),
                         'Tom Black 13 років, чоловік. Народився: 03.05.2010.')
        self.assertEqual(self.person_3.__str__(),
                         'Natali Kid 24 роки, жінка. Народилась: 15.09.1974. Померла: 14.09.1999.')

    def test_full_name(self):
        self.assertEqual(self.person_1.full_name, 'Иван Петров Сидорович')
        self.assertEqual(self.person_2.full_name, 'Tom Black')
        self.assertEqual(self.person_3.full_name, 'Natali Kid')

    def test_print_age(self):
        self.assertEqual(self.person_1.print_age, '43 роки')
        self.assertEqual(self.person_2.print_age, '13 років')
        self.assertEqual(self.person_3.print_age, '24 роки')

    def test_valid(self):
        self.assertTrue(self.person_1.valid())
        self.assertTrue(self.person_2.valid())
        self.assertTrue(self.person_3.valid())

        person_wrong_1 = Person('', '', '', '20.11.1980', '14.9.1999', 'm')
        self.assertFalse(person_wrong_1.valid())
        self.assertEqual(person_wrong_1.error, 'Вы не ввели ім\'я')

        person_wrong_2 = Person('Иван', '', '', '', '14.9.1999', 'm')
        self.assertFalse(person_wrong_2.valid())
        self.assertEqual(person_wrong_2.error, 'Помилка ввода дати народження')

        person_wrong_3 = Person('Natali', 'Kid', '', '15.9.1974', '14.9.1973', 'f')
        self.assertFalse(person_wrong_3.valid())
        self.assertEqual(person_wrong_3.error, "Вік не може бути від'ємним")

        person_wrong_4 = Person('Natali', 'Kid', '', '15.9.1974', '14.9.1975', 'ж')
        self.assertFalse(person_wrong_4.valid())
        self.assertEqual(person_wrong_4.error, 'Помилка ввода статі')


if __name__ == '__main__':
    unittest.main()
