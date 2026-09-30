"""Unit tests for shopping_cart.py."""
import io
import unittest
from unittest.mock import patch

from shopping_cart import CalculateTotal, display_total


class TestCalculateTotal(unittest.TestCase):
    """Tests for CalculateTotal()."""

    def test_empty_cart_returns_zero(self):
        self.assertEqual(CalculateTotal([]), 0)

    def test_single_item(self):
        cart = [{'name': 'Item A', 'price': 10.99}]
        self.assertAlmostEqual(CalculateTotal(cart), 10.99)

    def test_multiple_items_with_numeric_prices(self):
        cart = [
            {'name': 'Item A', 'price': 10.99},
            {'name': 'Item B', 'price': 5.99},
        ]
        self.assertAlmostEqual(CalculateTotal(cart), 16.98)

    def test_price_as_string_is_handled(self):
        cart = [
            {'name': 'Item A', 'price': 10.99},
            {'name': 'Item C', 'price': '8.49'},
        ]
        self.assertAlmostEqual(CalculateTotal(cart), 19.48)

    def test_invalid_price_raises_value_error(self):
        cart = [{'name': 'Item X', 'price': 'not-a-number'}]
        with self.assertRaises(ValueError):
            CalculateTotal(cart)


class TestDisplayTotal(unittest.TestCase):
    """Tests for display_total()."""

    def test_prints_total(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            display_total(25.47)
            self.assertEqual(fake_out.getvalue().strip(), "Total price: 25.47")


if __name__ == "__main__":
    unittest.main()
