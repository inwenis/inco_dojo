import unittest
from main import *

class TestMonkey(unittest.TestCase):
    def test_return_correct_set_of_letters(self):
        result = set_of_letters("B")
        self.assertEqual("AB", result)

    def test_return_correct_set_of_letters_singleton(self):
        result = set_of_letters("A")
        self.assertEqual("A", result)

    def test_return_correct_set_of_letters_abc(self):
        result = set_of_letters("C")
        self.assertEqual("ABC", result)

    def test_return_correct_diamond_A(self):
        result = indentNoOfSpaces("A", "A")
        self.assertEqual(0, result)

    def test_return_correct_diamond_C(self):
        result = indentNoOfSpaces("C", "A")
        self.assertEqual(2, result)

    def test_return_correct_diamond_up_to_c(self):
        result = diamond("C")
        self.assertEqual("  A\n B B\nC   C\n B B\n  A", result)

if __name__ == "__main__":
    unittest.main()
