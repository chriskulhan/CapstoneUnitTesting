import unittest
from pizza_calculator import PizzaCalculator

class TestPizzaCalculator(unittest.TestCase):
    def setUp(self):
        """Create a fresh PizzaCalculator for each test."""
        self.calculator = PizzaCalculator()

def test_calculate_pizzas_for_small_group(self):
    """Test pizza calculation for a small party of 5 people."""
    result = self.calculator.calculate_pizzas_needed(5)
    self.assertEqual(result, "5 people should need 2 pizzas")

def test_calculate_pizzas_for_large_group(self):
    """Test pizza calculation for a large party of 20 people."""
    result = self.calculator.calculate_pizzas_needed(20)
    self.assertEqual(result, "20 people should need 8 pizzas")

def test_negative_people_raises_error(self):
    """Test that negative numbers raise an error."""
    with self.assertRaises(ValueError):
        self.calculator.calculate_pizzas_needed(-5)

def test_is_enough_pizza_true(self):
    """Test that we definitely have enough pizza."""
    self.assertTrue(
        self.calculator.is_enough_pizza(5, 10),
        "5 pizzas should be enough for 10 people"
    )

def test_is_enough_pizza_false(self):
    """Test that we definitely don't have enough pizza."""
    self.assertFalse(
        self.calculator.is_enough_pizza(1, 10),
        "1 pizzas should not be enough for 10 people"
    )