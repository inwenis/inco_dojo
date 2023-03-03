import unittest
from main import *

class TestMonkey(unittest.TestCase):
    def test_empty_string(self):
        input = ""
        result = add(input)
        self.assertEqual(0, result)

    def test_single_number(self):
        input = "1"
        result = add(input)
        self.assertEqual(1, result)

    def test_two_numbers(self):
        input = "1,2"
        result = add(input)
        self.assertEqual(3, result)

    def test_more_than_two(self):
        input = "1,2,3"
        result = add(input)
        self.assertEqual(6, result)

    def test_two_numbers_separated_by_newline(self):
        input = "1\n2"
        result = add(input)
        self.assertEqual(3, result)

    def test_two_multi_digit_numbers_separated_by_newline(self):
        input = "30\n12"
        result = add(input)
        self.assertEqual(42, result)
    
    def test_more_than_two_numbers_only_separated_by_newline(self):
        input = "1\n2\n3"
        result = add(input)
        self.assertEqual(6, result)


if __name__ == "__main__":
    unittest.main()
