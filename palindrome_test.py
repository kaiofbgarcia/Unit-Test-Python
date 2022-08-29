import unittest
import palindrome

class TestPalindrome(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertEqual(palindrome.palindromo("reviver"), True)

    def test_is_not_palindrome(self):
        self.assertEqual(palindrome.palindromo("sacada"), False)

    def test_input_is_not_string(self):
        self.assertEqual(palindrome.palindromo(156), False)

if __name__ == '__name__':
    unittest.main()