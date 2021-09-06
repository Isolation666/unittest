import unittest
import math


class MathTest(unittest.TestCase):
    """Tests of the basic math function."""

    def test_sqrt(self):
        """ Tests the correct positive number square root """
        self.assertEqual(5, math.sqrt(25))
        self.assertEqual(0, math.sqrt(0))  # edge case
        self.assertEqual(3E+150, math.sqrt(9E+300))
        self.assertAlmostEqual(1.4142135623730951, math.sqrt(2), places=10)

    def test_pow(self):
        """ Tests the correct number power """
        self.assertEqual(9, math.pow(3, 2))
        self.assertEqual(1, math.pow(1, 100))

    def test_wrong_sqrt(self):
        """ Test the fail number power """
        self.assertEqual(1, math.sqrt(25))

    def test_sqrt_of_negative(self):
        """ Tests the square root negative number """
        with self.assertRaises(ValueError):
            result = math.sqrt(-1)

if __name__ == "__main__":
 unittest.main()