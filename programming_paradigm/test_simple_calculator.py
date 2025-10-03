import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(5,3),8)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5,3),2)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5,3),15)

    def test_division(self):
        self.assertEqual(self.calc.divide(15,3),5)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)



if __name__ == "__main__":
    unittest.main()