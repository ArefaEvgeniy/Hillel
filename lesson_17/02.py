import unittest
import sys

from task_01 import summa


class TestSumma(unittest.TestCase):

    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    def setUpClass(cls):
        print('setUpClass')

    def tearDownClass(cls):
        print('tearDownClass')

    def test_int_int(self):
        self.assertEqual(summa(4, 5), 9)
        self.assertEqual(summa(4, -4), 0)
        self.assertEqual(summa(4, 0), 4)

    @unittest.skipUnless(sys.platform.startswith("win"), 'this is Windows')
    def test_int_float(self):
        self.assertEqual(summa(4, 5.5), 9.5)
        self.assertEqual(summa(4, -0.5), 3.5)
        self.assertEqual(summa(4.0, 0), 4.0)

    def test_str(self):
        self.assertEqual(summa('4', '5.5'), '45.5')
        self.assertEqual(summa('4', '5'), '45')


class TestWrong(unittest.TestCase):

    @unittest.expectedFailure
    def test_wrong_data(self):
        self.assertEqual(summa('4', 5), 0)
        self.assertEqual(summa(4, None), None)


if __name__ == "__main__":
    unittest.main()
