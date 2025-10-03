import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        results = self.calc.add(5,3)
        self.assertEqual(results,8)

    def test_subtraction(self):
        results = self.calc.subtract(5,3)
        self.assertEqual(results,2)

    def test_multiplication(self):
        results = self.calc.multiply(5,3)
        self.assertEqual(results,15)

    def test_division(self):
        results = self.calc.divide(15,3)
        self.assertEqual(results,5)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)



if __name__ == "__main__":
    unittest.main()