import unittest
from messy_function import int_to_binary, every_other_char


class TestParenthesesToRemove(unittest.TestCase):
    def test_int_to_binary(self):
        self.assertEqual(int_to_binary(1), "1")
        self.assertEqual(int_to_binary(2), "10")
        self.assertEqual(int_to_binary(3), "11")
        self.assertEqual(int_to_binary(8), "1000")
        self.assertEqual(int_to_binary(30), "11110")

    def test_every_other_char(self):
        self.assertEqual(every_other_char(""), "")
        self.assertEqual(every_other_char("a"), "a")
        self.assertEqual(every_other_char("abc"), "ac")
        self.assertEqual(every_other_char("abcd"), "ac")


if __name__ == "__main__":
    unittest.main()
