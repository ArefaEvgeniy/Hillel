import unittest

from task_01 import summa, minus


class TestSumma(unittest.TestCase):

    def setUp(self):
        print('Before')

    def tearDown(self):
        print('After')

    def test_int_float(self):
        self.assertEqual(summa(4, 5), 9)
        self.assertEqual(summa(4, 0), 4)
        self.assertEqual(summa(4, -4), 0)
        self.assertEqual(summa(4, 5.0), 9.0)
        self.assertGreater(summa(4.03, 5), 9.02)
        self.assertLess(summa(4.03, 5), 9.04)
        self.assertEqual(round(summa(4.03, 5), 2), 9.03)

    @unittest.skip('Not fixed')
    def test_str(self):
        self.assertEqual(summa('4', '5'), '45')
        self.assertNotEquals(summa('4', '5'), '9')

    def test_wrong_data(self):
        self.assertEqual(summa(4, '5'), None)


class TestMinus(unittest.TestCase):

    def test_int_float(self):
        self.assertEqual(minus(4, 5), -1)
        self.assertEqual(minus(4, 0), 4)
        self.assertEqual(minus(4, -4), 8)
        self.assertEqual(minus(4, 5.0), -1.0)

    def test_wrong_data(self):
        with self.assertRaises(TypeError):
            minus(4, '5')


# if __name__ == '__main__':
#     unittest.main()
