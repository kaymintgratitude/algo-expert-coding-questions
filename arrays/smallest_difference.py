"""
Problem:        Smallest Difference
Description:    Write a function that takes in two non-empty arrays of integers, find the pair of numbers
                (one from each array) whose absolute difference is closest to zero, and returns an array
                containing these two numbers, with the number from the first array in the first position.

                Note that the absolute difference of two integers is the distance between them on the real
                number line. For example, the absolute difference of -5 and 5 is 10, and absolute difference
                of -5 and -4 is 1. 

                You can assume that there will only one pair of numbers with the smallest difference.

                Sample Input: 
                arrayOne = [-1, 5, 10, 20, 28, 3]
                arrayTwo = [26, 134, 135, 15, 17]

                Sample Output:
                [28, 26]

"""

import unittest


def smallest_difference(array_one, array_two):
    array_one.sort()
    array_two.sort()
    current = float("inf")
    minimum = float("inf")
    pointer_one, pointer_two = 0, 0
    smallest_pair = []

    while pointer_one < len(array_one) and pointer_two < len(array_two):
        difference = abs(array_one[pointer_one]-array_two[pointer_two])
        current = min(current, difference)

        if current < minimum:
            smallest_pair = [array_one[pointer_one], array_two[pointer_two]]
            minimum = current
        
        if array_one[pointer_one] < array_two[pointer_two]:
            pointer_one += 1
        elif array_one[pointer_one] > array_two[pointer_two]:
            pointer_two += 1
        else:
            pointer_one += 1
            pointer_two += 1
        
    return smallest_pair


class TestSmallestDifference(unittest.TestCase):
    def test_input_array_has_valid_smallest_difference(self):
        actual = smallest_difference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17])
        expected = [28, 26]
        self.assertEqual(expected, actual)

    def test_input_array_has_invalid_smallest_difference(self):
        actual = smallest_difference([], [10, 11])
        expected = []
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()