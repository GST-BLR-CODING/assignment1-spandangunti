"""
Given a string digits containing 2 to 9 inclusive, return all possible strings it could represent when mapping to letters on a phone dialpad.
These are the mappings on a phone dialpad:

| 2 | abc  |
| 3 | def  |
| 4 | ghi  |
| 5 | jkl  |
| 6 | mno  |
| 7 | pqrs |
| 8 | tuv  |
| 9 | wxyz |
Example 1:
Input: digits = "23"
Output: ['ab', 'ac', 'ad', 'ae', 'af', 'ba', 'bc', 'bd', 'be', 'bf', 'ca', 'cb', 'cd', 'ce', 'cf', 'da', 'db', 'dc', 'de', 'df', 'ea', 'eb', 'ec', 'ed', 'ef', 'fa', 'fb', 'fc', 'fd', 'fe']

"""

import unittest
import itertools
# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def dialpad(n):
    pass #WRITE YOUR CODE FROM HERE BY REMOVING 'pass' KEYWORD
    


# DO NOT TOUCH THE BELOW CODE
class TestRunThis(unittest.TestCase):

    def test_01(self):
        self.assertEqual(dialpad('23'), ['ab', 'ac', 'ad', 'ae', 'af', 'ba', 'bc', 'bd', 'be', 'bf', 'ca', 'cb', 'cd', 'ce', 'cf', 'da', 'db', 'dc', 'de', 'df', 'ea', 'eb', 'ec', 'ed', 'ef', 'fa', 'fb', 'fc', 'fd', 'fe'])

    def test_02(self):
        self.assertEqual(dialpad('42'), ['gh', 'gi', 'ga', 'gb', 'gc', 'hg', 'hi', 'ha', 'hb', 'hc', 'ig', 'ih', 'ia', 'ib', 'ic', 'ag', 'ah', 'ai', 'ab', 'ac', 'bg', 'bh', 'bi', 'ba', 'bc', 'cg', 'ch', 'ci', 'ca', 'cb'])

    

if __name__ == '__main__':
    unittest.main(verbosity=2)
