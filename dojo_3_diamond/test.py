import unittest
from main import *

class TestMonkey(unittest.TestCase):
    def test_for_a_returns_a(self):
        result = diamond("A")
        self.assertEqual("A", result)

    def test_return_correct_set_of_letters(self):
        result = set_of_letters("B")
        self.assertEqual("AB", result)

    def test_return_correct_set_of_letters_singleton(self):
        result = set_of_letters("A")
        self.assertEqual("A", result)

    def test_return_correct_set_of_letters_abc(self):
        result = set_of_letters("C")
        self.assertEqual("ABC", result)

    def test_return_correct_letters_in_order(self):
        result = diamond("C")
        self.assertEqual("ABCBA", result)
if __name__ == "__main__":
    unittest.main()
