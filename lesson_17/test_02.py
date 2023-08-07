import unittest

from task_01 import summa


class TestSumma2(unittest.TestCase):

    def test_correct_data_2(self):
        self.assertEqual(summa(1, 2), 3)
        self.assertEqual(summa(1.2, 2.8), 4.0)

    def test_wrong_data_2(self):
        self.assertIsNone(summa(False, '5'))
