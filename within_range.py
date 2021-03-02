"""
Find out the even numbers in the given range and print all possible permutations of length 3 for the same numbers.

Example 1
Input
start = 2
stop = 8

Output
[(2, 4, 6), (2, 6, 4), (4, 2, 6), (4, 6, 2), (6, 2, 4), (6, 4, 2)]

"""


import unittest
import itertools

# Implement the below function and run this file
# Return the output, No need read input or print the ouput

#WRITE YOUR CODE FROM HERE BY REMOVING 'pass' KEYWORD
def within_range(start,stop):
    pass


# DO NOT TOUCH THE BELOW CODE
class TestIsPrime(unittest.TestCase):

    def test_01(self):
        self.assertEqual(within_range(2,8), [(2, 4, 6), (2, 6, 4), (4, 2, 6), (4, 6, 2), (6, 2, 4), (6, 4, 2)])

    def test_02(self):
        self.assertEqual(within_range(6,12), [(6, 8, 10), (6, 10, 8), (8, 6, 10), (8, 10, 6), (10, 6, 8), (10, 8, 6)])

    def test_03(self):
        self.assertEqual(within_range(14,23), [(14, 16, 18), (14, 16, 20), (14, 16, 22), (14, 18, 16), (14, 18, 20), (14, 18, 22), (14, 20, 16), (14, 20, 18), (14, 20, 22), (14, 22, 16), (14, 22, 18), (14, 22, 20), (16, 14, 18), (16, 14, 20), (16, 14, 22), (16, 18, 14), (16, 18, 20), (16, 18, 22), (16, 20, 14), (16, 20, 18), (16, 20, 22), (16, 22, 14), (16, 22, 18), (16, 22, 20), (18, 14, 16), (18, 14, 20), (18, 14, 22), (18, 16, 14), (18, 16, 20), (18, 16, 22), (18, 20, 14), (18, 20, 16), (18, 20, 22), (18, 22, 14), (18, 22, 16), (18, 22, 20), (20, 14, 16), (20, 14, 18), (20, 14, 22), (20, 16, 14), (20, 16, 18), (20, 16, 22), (20, 18, 14), (20, 18, 16), (20, 18, 22), (20, 22, 14), (20, 22, 16), (20, 22, 18), (22, 14, 16), (22, 14, 18), (22, 14, 20), (22, 16, 14), (22, 16, 18), (22, 16, 20), (22, 18, 14), (22, 18, 16), (22, 18, 20), (22, 20, 14), (22, 20, 16), (22, 20, 18)])


if __name__ == '__main__':
    unittest.main(verbosity=2)
