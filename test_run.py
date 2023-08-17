import unittest

from run import minus


class TestAdd(unittest.TestCase):

    def test_add_function(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(4, 7), 11)

    def test_add_function_with_floats(self):
        self.assertAlmostEqual(add(2.1, 5.2), 7.3)


if __name__ == "__main__":
    unittest.main()