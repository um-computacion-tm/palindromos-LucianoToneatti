import unittest

def palindro(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] == palabra[-1]:
        return palindro (palabra[1:-1])
    else:
        return False

class TestPalindrome(unittest.TestCase):

    def test_palindrome_simple1(self):
        result = palindro('neuquen')
        self.assertEqual(result, True)
    def test_palindrome_simple2(self):
        result = palindro('oso')
        self.assertEqual(result, True)
    def test_palindrome_simple3(self):
        result = palindro('radar')
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()