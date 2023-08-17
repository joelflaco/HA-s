import unittest

from run import minus


class TestMinus(unittest.TestCase):

    def test_minus_function(self):
        self.assertEqual(minus(1, 2), 3)
        self.assertEqual(minus(4, 7), 11)

    def test_minus_function_with_floats(self):
        self.assertAlmostEqual(minus(2.1, 5.2), 7.3)


if __name__ == "__main__":
    unittest.main()
