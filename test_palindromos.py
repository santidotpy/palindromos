import unittest
from palindromos import is_palindrome


class Test_Is_Palindrome(unittest.TestCase):
    
    def test_palindrome_word(self):
        self.assertTrue(is_palindrome('hannah'))

    def test_palindrome_capital(self):
        self.assertTrue(is_palindrome('Hannah'))
    
    def test_palindrome_multiple_capitals(self):
        self.assertTrue(is_palindrome('HaNNaH'))
    
    def test_palindrome_spaces(self):
        self.assertTrue(is_palindrome('H a N N a H'))

    def test_no_palindrome_word(self):
        self.assertFalse(is_palindrome('john'))

    def test_no_palindrome_capital(self):
        self.assertFalse(is_palindrome('Johnny'))

    def test_no_palindrome_multiple_capitals(self):
        self.assertFalse(is_palindrome('eXaMpLe'))

    def test_no_palindrome_spaces(self):
        self.assertFalse(is_palindrome('Not A Palindrome'))

    def test_palindrome_number(self):
        self.assertTrue(is_palindrome(123321))

    def test_palindrome_number_string(self):
        self.assertTrue(is_palindrome('123321'))

    def test_palindrome_spaces_number_string(self):
        self.assertTrue(is_palindrome('12 33 21'))

    def test_no_palindrome_number(self):
        self.assertFalse(is_palindrome(1829387123))

    def test_no_palindrome_number_string(self):
        self.assertFalse(is_palindrome('781623'))

    def test_no_palindrome_spaces_number_string(self):
        self.assertFalse(is_palindrome('781 62 3'))


if __name__ == '__main__':
    unittest.main()
