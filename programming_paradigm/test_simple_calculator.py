import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.SimpleCalculator = SimpleCalculator()

    def test_add(self):
        results = self.SimpleCalculator.add(5,3)
        self.assertEqual(results,8)

    def test_subtract(self):
        results = self.SimpleCalculator.subtract(5,3)
        self.assertEqual(results,2)

    def test_multiply(self):
        results = self.SimpleCalculator.multiply(5,3)
        self.assertEqual(results,15)

    def test_divide(self):
        results = self.SimpleCalculator.divide(15,3)
        self.assertEqual(results,5)
        with self.assertRaises(ZeroDivisionError):
            self.SimpleCalculator.divide(10, 0)



if __name__ == "__main__":
    unittest.main()