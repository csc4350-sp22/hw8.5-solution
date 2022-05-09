import unittest
from parentheses import parentheses_to_remove


class TestParenthesesToRemove(unittest.TestCase):
    def test_parentheses_to_remove_1(self):
        """
        Test trivial case.
        """
        self.assertEqual(parentheses_to_remove(""), 0)
        self.assertEqual(parentheses_to_remove("aaa"), 0)

    def test_parentheses_to_remove_2(self):
        """
        Test balanced cases.
        """
        self.assertEqual(parentheses_to_remove("abc()"), 0)
        self.assertEqual(parentheses_to_remove("()()"), 0)
        self.assertEqual(parentheses_to_remove("(())()"), 0)
        self.assertEqual(parentheses_to_remove("((())())"), 0)

    def test_parentheses_to_remove_3(self):
        """
        Test unbalanced cases.
        """
        self.assertEqual(parentheses_to_remove("("), 1)
        self.assertEqual(parentheses_to_remove("(("), 2)
        self.assertEqual(parentheses_to_remove(")("), 2)
        self.assertEqual(parentheses_to_remove("(()"), 1)


if __name__ == "__main__":
    unittest.main()
