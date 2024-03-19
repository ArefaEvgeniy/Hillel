import sys
import unittest

from task_01 import summa, mines


class TestSumma(unittest.TestCase):

    def test_int_float(self):
        self.assertEqual(summa(3, 4), 7)
        self.assertEqual(summa(3, 0), 3)
        self.assertEqual(summa(3, -3), 0)
        self.assertEqual(summa(3, 1.3), 4.3)
        self.assertEqual(summa(-1.3, 2.2), 0.9)

    def test_string(self):
        self.assertEqual(summa('3', '4'), '34')
        self.assertEqual(summa('aas', 'e'), 'aase')

    def test_wrong_data(self):
        self.assertEqual(summa('3', 4), None)
        self.assertEqual(summa('3', None), None)
        self.assertEqual(summa(3, None), None)


class TestMines(unittest.TestCase):

    # def setUp(self):
    #     print('Start')
    #
    # def tearDown(self):
    #     print('End')

    # @unittest.skipUnless(sys.platform.startswith('win'), 'not supported Unix')
    # @unittest.expectedFailure
    def test_int_float(self):
        self.assertEqual(mines(3, 4), -1)
        self.assertEqual(mines(3, 0), 3)
        self.assertEqual(mines(3, -3), 6)
        self.assertEqual(mines(3, 1.3), 1.7)
        self.assertEqual(round(mines(4, 2.34), 3), 1.66)

    def test_wrong_data(self):
        with self.assertRaises(TypeError):
            mines('3', 4)
