import unittest
from calc_mul import calc

class TestCalc(unittest.TestCase):

    def test_positive_integers(self):
        self.assertEqual(calc(3, 7), 21)

    def test_string_inputs(self):
        self.assertEqual(calc('a', 'b'), -1)

    def test_decimal_inputs(self):
        self.assertEqual(calc(0.1, 999), -1)

    def test_out_of_range_integers(self):
        self.assertEqual(calc(0, 150), -1)

    def test_zero_multiplication(self):
        self.assertEqual(calc(0, 1), -1)

    def test_max_range_multiplication(self):
        self.assertEqual(calc(998, 999), 997002)

    def test_near_max_range_multiplication(self):
        self.assertEqual(calc(999, 999), -1)

    def test_negative_and_positive_input(self):
        self.assertEqual(calc(-1, 1), -1)

    def test_large_positive_input(self):
        self.assertEqual(calc(1, 1000), -1)

if __name__ == '__main__':
    unittest.main()