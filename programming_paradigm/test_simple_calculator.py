import unittest
from simple_calculator import SimpleCalculator 

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculate = SimpleCalculator()
    def test_addition (self):
        result = self.calculate.add(5,3)
        self.assertEqual(result, 8)
    def test_subtract(self):
        result = self.calculate.subtract(5,3)
        self.assertEqual(result, 2)
        
    def test_multiply(self):
        result = self.calculate.multiply(5,3)
        self.assertEqual(result, 15)

    def test_divide(self):
        result = self.calculate.divide(6,3)
        self.assertEqual(result, 2)

    def test_divide_by_zero(self):
        result = self.calculate.divide(5, 0)
        self.assertEqual(result, None)

if __name__ == "__main__":
    unittest.main()