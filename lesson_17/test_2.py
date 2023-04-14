import unittest
from task_01 import mines


class TestMines(unittest.TestCase):

    def setUp(self) -> None:
        ...

    def tearDown(self) -> None:
        ...

    # def setUpClass(cls) -> None:
    #     ...
    #
    # def tearDownClass(cls) -> None:
    #     ...

    # @unittest.expectedFailure
    def test_int_data(self):
        self.assertEqual(mines(4, 5), -1)
        self.assertEqual(mines(5, 0), 5)
        self.assertEqual(mines(-1, -2), 1)

    # @unittest.skip('Not release yet')
    def test_float_data(self):
        self.assertEqual(mines(4.5, 1), 3.5)
        self.assertEqual(mines(4.5, 0), 4.5)
        self.assertEqual(round(mines(4, 2.34), 2), 1.66)


class Wrong(unittest.TestCase):

    def test_wrong_data(self):
        with self.assertRaises(TypeError):
            mines(4.5, '1')
        with self.assertRaises(TypeError):
            mines(4.5, None)


if __name__ == "__main__":
    unittest.main()
