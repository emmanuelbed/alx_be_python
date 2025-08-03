import unittest
from simple_calculator import SimpleCalculator 

class TestCalculator(unittest.TestCase):
    self.Simplecalculator = SimpleCalculator()
    def test_addition(self):
        result = SimpleCalculator.add(self, 5,3)
        self.assertEqual(result, 8)
    def test_subtract(self):
        result = SimpleCalculator.subtract(self, 5,3)
        self.assertEqual(result, 2)
        
    def test_multiply(self):
        result = SimpleCalculator.multiply(self, 5,3)
        self.assertEqual(result, 15)

    def test_divide(self):
        result = SimpleCalculator.divide(self, 6,3)
        self.assertEqual(result, 2)

    def test_divide_by_zero(self):
        result = SimpleCalculator.divide(self, 5, 0)
        self.assertEqual(result, None)

if __name__ == "__main__":
    unittest.main()