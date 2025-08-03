import unittest
from simple_calculator import SimpleCalculator 

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(5,3), 8)

    def test_subtract(self):
        result = self.calc.subtract(5,3)
        self.assertEqual(result, 2)
        
    def test_multiply(self):
        result = self.calc.multiply(5,3)
        self.assertEqual(result, 15)

    def test_divide(self):
        result = self.calc.divide(6,3)
        self.assertEqual(result, 2)

    def test_divide_by_zero(self):
        result = self.calc.divide(5, 0)
        self.assertEqual(result, None)

if __name__ == "__main__":
    unittest.main()