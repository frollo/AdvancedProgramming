from unittest import TestCase
from unittest import main
from es1 import TicTacToe

class TestingString(TestCase):
    def testAnagram(self):
        palindromestrings = [TicTacToe("Do Geese see God?"), TicTacToe("Rise to vote, sir")]
        nonpalindromestrings = [TicTacToe("String"), TicTacToe("FooBar")]
        for p in palindromestrings:
            self.assertTrue(p.isPalindrome())
        for np in nonpalindromestrings:
            self.assertFalse(np.isPalindrome())

    def testValidate(self):
        strings = [(TicTacToe("XOXXXOOOX"), "X"), (TicTacToe("XOXOOX"), "Moves"),
        (TicTacToe("  OXXXOOO"), "Invalid"), (TicTacToe("X OXOXX O"), "X"), (TicTacToe("   OOOOXXX"), "Invalid")]
        for s in strings:
            self.assertEquals(s[0].validate(), s[1])


if __name__ == '__main__':
    main()
