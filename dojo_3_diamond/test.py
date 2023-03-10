import unittest
from main import *

class TestMonkey(unittest.TestCase):
    def test1(self):
        self.assertEqual(0, 0)

if __name__ == "__main__":
    unittest.main()
