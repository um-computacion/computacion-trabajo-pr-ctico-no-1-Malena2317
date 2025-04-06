import unittest

def roman_to_decimal(roman):
    pass

class TestDecimalToRoman(unittest.TestCase):

    def test_basic_numbers(self):
        self.assertEqual(roman_to_decimal("I"), 1)
        self.assertEqual(roman_to_decimal("II"), 2)
        self.assertEqual(roman_to_decimal("III"), 3)
        self.assertEqual(roman_to_decimal("V"), 5)
        self.assertEqual(roman_to_decimal("X"), 10)

    def test_subtraction_rules(self):
        self.assertEqual(roman_to_decimal("IV"), 4)
        self.assertEqual(roman_to_decimal("IX"), 9)
        self.assertEqual(roman_to_decimal("XL"), 40)
        self.assertEqual(roman_to_decimal("XC"), 90)

    def test_complex_numbers(self):
        self.assertEqual(roman_to_decimal("XIV"), 14)
        self.assertEqual(roman_to_decimal("XIX"), 19)
        self.assertEqual(roman_to_decimal("L"), 50)
        self.assertEqual(roman_to_decimal("C"), 100)
        self.assertEqual(roman_to_decimal("D"), 500)
        self.assertEqual(roman_to_decimal("M"), 1000)
        self.assertEqual(roman_to_decimal("MCMXCIX"), 1999)

if __name__ == "__main__":
    unittest.main()
    