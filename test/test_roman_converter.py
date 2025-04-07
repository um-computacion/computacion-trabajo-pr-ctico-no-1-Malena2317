import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from roman_converter import decimal_to_roman
import unittest

class TestDecimalToRoman(unittest.TestCase):

    def test_basic_numbers(self):
        self.assertEqual(decimal_to_roman(1), "I")
        self.assertEqual(decimal_to_roman(2), "II")
        self.assertEqual(decimal_to_roman(3), "III")
        self.assertEqual(decimal_to_roman(5), "V")
        self.assertEqual(decimal_to_roman(10), "X")

    def test_subtraction_rules(self):
        self.assertEqual(decimal_to_roman(4), "IV")
        self.assertEqual(decimal_to_roman(9), "IX")
        self.assertEqual(decimal_to_roman(40), "XL")
        self.assertEqual(decimal_to_roman(90), "XC")

    def test_complex_number(self):
        self.assertEqual(decimal_to_roman(14), "XIV")
        self.assertEqual(decimal_to_roman(19), "XIX")
        self.assertEqual(decimal_to_roman(50), "L")
        self.assertEqual(decimal_to_roman(100), "C")
        self.assertEqual(decimal_to_roman(500), "D")
        self.assertEqual(decimal_to_roman(1000), "M")
        self.assertEqual(decimal_to_roman(1999), "MCMXCIX")

    def test_upper_limit(self):
        self.assertEqual(decimal_to_roman(3999), "MMMCMXCIX")

if __name__ == "__main__":
    unittest.main()
    