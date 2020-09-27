"""
Problem:        Is Valid Subsequence
Description:    Given two non-empty arrays of integers, write a function that determines whether the second is a 
                subsequence of the first one.

                A subsequence of an array is a set of number that aren't necessarily adjacent in the array but that
                are in the same order they appear in the array. For instance, the numbers [1, 3, 4] form a 
                subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4]. Note that a single number in an 
                array and the array itself are both valid subsequences of the array.

                Sample Input
                array = [5, 1, 22, 25, 25, 6, -1, 8, 10]
                subsequence = [1, 6, -1 , 10]

                Sample Output
                true

"""

import unittest


def is_valid_subsequence(array, sequence):
    aux = []

    for num in array:
        if num in sequence and len(aux) < len(sequence):
            aux.append(num)

    return aux == sequence


class TestIsValidSubsequence(unittest.TestCase):
    def test_input_array_has_valid_subsequence(self):
        actual = is_valid_subsequence([5, 1, 22, 25, 25, 6, -1, 8, 10], [1, 6, -1, 10])
        self.assertTrue(actual)

    def test_input_array_has_invalid_subsequence(self):
        actual = is_valid_subsequence([], [10])
        self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()