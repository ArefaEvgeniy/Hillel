import unittest

from task_01 import summa, mines


class TestSumma(unittest.TestCase):

    # def setUp(self) -> None:
    #     print('SET-UP')
    #
    # def tearDown(self) -> None:
    #     print('TEAR-DOWN')

    # def setUpClass(cls) -> None:
    #     ...
    #
    # def tearDownClass(cls) -> None:
    #     ...

    def test_correct_data(self):
        self.assertEqual(summa(4, 5), 9)
        self.assertNotEqual(summa(4, 5), 0)
        self.assertLess(summa(4, 5), 10)

    # @unittest.expectedFailure
    def test_wrong_data(self):
        self.assertEqual(summa(4, None), None)
        self.assertIsNone(summa(4, '5'))

    def test_string_data(self):
        self.assertEqual(summa('aaa', 'bb'), 'aaabb')
        self.assertEqual(summa('4', '5'), '45')


class TestMines(unittest.TestCase):

    @unittest.skip('Not implemented yet')
    def test_int_float(self):
        self.assertEqual(mines(4, 5), -1)
        self.assertEqual(mines(3, 3), 0)
        self.assertEqual(mines(4, 0), 4)
        self.assertEqual(mines(4, 0.5), 3.5)
        self.assertEqual(round(mines(4.2, 5.1), 1), -0.9)

    def test_wrong_data(self):
        with self.assertRaises(TypeError):
            mines(4, '5')


if __name__ == "__main__":
    unittest.main()
