#!/usr/bin/env python3
"""
Simple tests for the demoprogram package.
"""

import unittest
from demoprogram import utility, calc


class TestUtilityFunctions(unittest.TestCase):
    """Test cases for utility functions."""
    
    def test_reverse_string(self):
        """Test string reversal."""
        self.assertEqual(utility.reverse_string("hello"), "olleh")
        self.assertEqual(utility.reverse_string(""), "")
        self.assertEqual(utility.reverse_string("123"), "321")
    
    def test_is_palindrome(self):
        """Test palindrome detection."""
        self.assertTrue(utility.is_palindrome("racecar"))
        self.assertTrue(utility.is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(utility.is_palindrome("hello"))
        self.assertTrue(utility.is_palindrome(""))
    
    def test_count_words(self):
        """Test word counting."""
        self.assertEqual(utility.count_words("hello world"), 2)
        self.assertEqual(utility.count_words(""), 0)
        self.assertEqual(utility.count_words("single"), 1)
    
    def test_get_system_info(self):
        """Test system info retrieval."""
        info = utility.get_system_info()
        self.assertIn('platform', info)
        self.assertIn('python_version', info)
        self.assertIn('executable', info)


class TestCalcFunctions(unittest.TestCase):
    """Test cases for arithmetic functions."""
    
    def test_basic_arithmetic(self):
        """Test basic arithmetic operations."""
        self.assertEqual(calc.add(5, 3), 8)
        self.assertEqual(calc.subtract(5, 3), 2)
        self.assertEqual(calc.multiply(5, 3), 15)
        self.assertEqual(calc.divide(6, 2), 3.0)
        self.assertEqual(calc.power(2, 3), 8)
    
    def test_division_by_zero(self):
        """Test division by zero error."""
        with self.assertRaises(ZeroDivisionError):
            calc.divide(10, 0)
    
    def test_square_root(self):
        """Test square root calculation."""
        self.assertEqual(calc.square_root(4), 2.0)
        self.assertEqual(calc.square_root(0), 0.0)
        with self.assertRaises(ValueError):
            calc.square_root(-1)
    
    def test_factorial(self):
        """Test factorial calculation."""
        self.assertEqual(calc.factorial(0), 1)
        self.assertEqual(calc.factorial(1), 1)
        self.assertEqual(calc.factorial(5), 120)
        with self.assertRaises(ValueError):
            calc.factorial(-1)
    
    def test_gcd_lcm(self):
        """Test GCD and LCM calculations."""
        self.assertEqual(calc.gcd(12, 18), 6)
        self.assertEqual(calc.lcm(12, 18), 36)
    
    def test_average(self):
        """Test average calculation."""
        self.assertEqual(calc.average([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(calc.average([10]), 10.0)
        with self.assertRaises(ValueError):
            calc.average([])
    
    def test_percentage(self):
        """Test percentage calculation."""
        self.assertEqual(calc.percentage(25, 100), 0.25)
        self.assertEqual(calc.percentage(50, 200), 0.25)
        with self.assertRaises(ZeroDivisionError):
            calc.percentage(10, 0)
    
    def test_round_to_decimal(self):
        """Test decimal rounding."""
        self.assertEqual(calc.round_to_decimal(3.14159, 2), 3.14)
        self.assertEqual(calc.round_to_decimal(3.14159, 4), 3.1416)


if __name__ == "__main__":
    unittest.main() 