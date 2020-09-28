"""
Problem:        Monotonic Array
Description:    Write a function that takes in an array of integers and returns a boolean representing 
                whether the array is monotonic.

                An array is said to be monotonic if its elements, from left to right, are entirely non-increasing
                or entirely non-increasing. 

                Non-increasing elements aren't necessarily exclusively decreasing; they simply don't increase.
                Similarly, non-decreasing elements aren't necessarily exclusively increasing; they simply don't decrease.

                Note that empty arrays and arrays of one element are monotonic.

                Sample Input
                array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

                Sample Output
                true

"""

import unittest


def is_monotonic(arr):
    if len(arr) <= 2:
        return True
    difference_set = set()
    i = 1
    while i < len(arr):
        difference = arr[i] - arr[i - 1]
        if difference > 0:
            difference_set.add(1)
        elif difference < 0:
            difference_set.add(-1)
        else:
            difference_set.add(0)

        if difference > 0 and -1 in difference_set:
            return False
        if difference < 0 and 1 in difference_set:
            return False
        i += 1

    return True


class TestIsMonotonic(unittest.TestCase):
    def test_input_array_has_valid_is_monotonic(self):
        actual = is_monotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001])
        self.assertTrue(actual)

    def test_input_array_has_invalid_is_monotonic(self):
        actual = is_monotonic([-1, 5, 4, 8])
        self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()
