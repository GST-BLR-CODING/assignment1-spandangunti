"""
Read a number from the user and if the number is perfect number, then find all the possible permutations of its divisors restricted to length 2

Example 1
Input
num = 6

Output
[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

Example 2
Input
num = 27

Output
The given number is not a perfect number

"""


import unittest
import itertools

# Implement the below function and run this file
# Return the output, No need read input or print the ouput

#WRITE YOUR CODE FROM HERE BY REMOVING 'pass' KEYWORD
def divisors_of_perfect(num):
    list2 = []
    for i in range(1,num):
        if num%i==0:
            list2.append(i)
# print(list2)
    if sum(list2) == num:
        permutation1 = itertools.permutations(list2,2)
        return list(permutation1)
    else:
        return "The given number is not a perfect number"


# DO NOT TOUCH THE BELOW CODE
class TestIsPrime(unittest.TestCase):

    def test_01(self):
        self.assertEqual(divisors_of_perfect(6), [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])

    def test_02(self):
        self.assertEqual(divisors_of_perfect(27), "The given number is not a perfect number")

    def test_03(self):
        self.assertEqual(divisors_of_perfect(28), [(1, 2), (1, 4), (1, 7), (1, 14), (2, 1), (2, 4), (2, 7), (2, 14), (4, 1), (4, 2), (4, 7), (4, 14), (7, 1), (7, 2), (7, 4), (7, 14), (14, 1), (14, 2), (14, 4), (14, 7)])


if __name__ == '__main__':
    unittest.main(verbosity=2)
