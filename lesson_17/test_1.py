import unittest
from task_01 import summa


class TestSumma(unittest.TestCase):

    def test_int_data(self):
        self.assertEqual(summa(4, 5), 9)
        self.assertEqual(summa(-5, 5), 0)
        self.assertEqual(summa(-5, 0), -5)

    def test_float_data(self):
        self.assertEqual(summa(-1.2, -3.4), -4.6)
        self.assertEqual(summa(1, 1.2), 2.2)

    def test_wrong_data(self):
        self.assertEqual(summa(4, '5'), None)
        self.assertEqual(summa(4, None), None)

    def test_str_data(self):
        self.assertEqual(summa('1', '2'), '12')
        self.assertEqual(summa('0', '-1.2'), '0-1.2')


if __name__ == "__main__":
    unittest.main()
