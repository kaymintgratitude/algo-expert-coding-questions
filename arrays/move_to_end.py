"""
Problem:        Move Element To End
Description:    You're given an array of integers and an integer. Write a function
                that moves all instances of that integer in the array to the end of the array
                and returns the array.

                The function should perform this in place (i.e., it should mutate the input array)
                and doesn't need to maintain the order of the other integers.

                Sample Input
                array = [2, 1, 2, 2, 2, 3, 4, 2]
                toMove = 2

                Sample Output
                [1, 3, 4, 2, 2, 2, 2, 2]

"""

import unittest


def move_element_to_end(arr, to_move):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    start = 0
    end = len(arr) - 1

    while start < end:
        if arr[start] == to_move:
            if arr[end] == to_move:
                end -= 1
            else:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        else:
            start += 1

    return arr


class TestSmallestDifference(unittest.TestCase):
    def test_input_array_has_valid_move_to_end(self):
        actual = move_element_to_end([2, 1, 2, 2, 2, 3, 4, 2], 2)
        expected = [4, 1, 3, 2, 2, 2, 2, 2]
        self.assertListEqual(expected[:-5], actual[:-5])

    def test_input_array_has_invalid_move_to_end(self):
        actual = move_element_to_end([1, 2, 3, 4, 5], 10)
        expected = [1, 2, 3, 4, 5]
        self.assertListEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()