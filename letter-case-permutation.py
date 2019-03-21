import unittest
import itertools

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        : rtype: List[str]
        """
        L = [[i.lower(), i.upper()] if i.isalpha() else i for i in S]
        return [''.join(i) for i in itertools.product(*L)]

class Test(unittest.TestCase):

    def test_only_numbers(self):
        solution = Solution()
        actual = solution.letterCasePermutation('1234')
        expected = ['1234']
        self.assertEqual(actual, expected)

    def test_one_letter(self):
        solution = Solution()
        actual = solution.letterCasePermutation('1a234')
        expected = ['1a234', '1A234']
        self.assertEqual(actual, expected)

    def test_multiple_letters(self):
        solution = Solution()
        actual = solution.letterCasePermutation('1a2b34')
        expected = ['1a2b34', '1a2B34','1A2b34','1A2B34',]
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)