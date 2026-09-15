import unittest

from palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(is_palindrome(121))
        self.assertFalse(is_palindrome(31))

    def test_one_digit(self):
        for n in range(1, 10):
            self.assertTrue(is_palindrome(n))

    def test_even_length(self):
        self.assertTrue(is_palindrome(1221))
        self.assertFalse(is_palindrome(1231))

    def test_trailing_zero(self):
        self.assertFalse(is_palindrome(10))
        self.assertFalse(is_palindrome(1000021))

    def test_big(self):
        self.assertTrue(is_palindrome(1234554321))
        self.assertTrue(is_palindrome(10**18 + 1))
        self.assertFalse(is_palindrome(10**18 + 2))


if __name__ == "__main__":
    unittest.main(verbosity=2)
