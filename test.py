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

if __name__ == "__main__":
    unittest.main()
