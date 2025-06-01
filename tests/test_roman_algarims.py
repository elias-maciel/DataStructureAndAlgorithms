import unittest

from datastructuresandalgorithms.leet_codes.roman_algarisms import Solution


class MyTestCase(unittest.TestCase):
    service = Solution()

    def test_symbol_is_empty(self):
        symbol = ""
        expected = 0
        actual = self.service.roman_algarisms_to_int(symbol)
        self.assertEqual(expected, actual)

    def test_single_letter_symbol(self):
        symbol = "I"
        expected = 1
        actual = self.service.roman_algarisms_to_int(symbol)
        self.assertEqual(expected, actual)

    def test_multiple_letter_symbol(self):
        symbol = "LVIII"
        expected = 58
        actual = self.service.roman_algarisms_to_int(symbol)
        self.assertEqual(expected, actual)

    def test_fully_complex_symbol(self):
        symbol = "MCMXCIV"
        expected = 1994
        actual = self.service.roman_algarisms_to_int(symbol)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
