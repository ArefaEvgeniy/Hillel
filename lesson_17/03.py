import unittest

from task_01 import mines


class TestMines(unittest.TestCase):
    def test_int_float(self):
        self.assertEqual(mines(4, 5), -1)
        self.assertEqual(mines(4, 0.5), 3.5)
        self.assertEqual(mines(4, 4), 0)
        self.assertEqual(round(mines(4, 2.34), 3), 1.66)

    def test_wrong_data(self):
        with self.assertRaises(TypeError):
            mines(4, '5')

        with self.assertRaises(TypeError):
            mines('4', '5')


if __name__ == "__main__":
    unittest.main()
