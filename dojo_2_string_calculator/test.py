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

    def test_more_than_two_numbers_mixed_separators(self):
        input = "1,2\n3"
        result = add(input)
        self.assertEqual(6, result)

    def test_should_work_for_single_delimiter_specified_in_input_and_no_value(self):
        input = "//;\n"
        result = add(input)
        self.assertEqual(0, result)

    def test_should_work_for_single_delimiter_specified_in_input_and_some_values(self):
        input = "//;\n1;2;3"
        result = add(input)
        self.assertEqual(6, result)

    def test_dont_allow_a_single_negative_number_and_throw_meaningful_exception(self):
        input = "-1"
        with self.assertRaises(Exception) as cm:
            add(input)
        self.assertIn("negatives not allowed: -1", str(cm.exception))

    def test_dont_allow_single_negative_number_exception_doesnt_contain_positive_number(self):
        input = "-1,2"
        with self.assertRaises(Exception) as cm:
            add(input)
        self.assertNotIn("2", str(cm.exception))

    def test_ignore_single_number_above_1000(self):
        input = "1001"
        result = add(input)
        self.assertEqual(0, result)

if __name__ == "__main__":
    unittest.main()
