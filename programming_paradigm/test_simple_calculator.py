import unittest
class SimpleCalculator:
    """A simple calculator class that supports basic arithmetic operations."""

    def add(self, a, b):
        """Return the addition of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the subtraction of b from a."""
        return a - b

    def multiply(self, a, b):
        """Return the multiplication of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the division of a by b. Returns None if b is zero."""
        if b == 0:
            return None
        return a / b

class TestCalculator(unittest.TestCase):
    def test_add(self):
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