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
        result = letters("C")
        self.assertEqual("ABCBA", result)

    def test_return_correct_diamond_rows_up_to_b(self):
        result = add_new_lines(letters("B"))
        self.assertEqual("A\nB B\nA", result)


if __name__ == "__main__":
    unittest.main()
