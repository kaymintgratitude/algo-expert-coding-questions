"""
Problem:        Longest Peak
Description:    Write a function that takes in an array of integers and returns the length of the longest
                peak in the array.

                A peak is defined as adjacent integers in the array that are strictly increasing until they
                reach a tip (the highest value in the peak), at which point they become strictly decreasing.
                At least three integers are required to form a peak.

                For example, the integers 1,4,10,2 form a peak, but the integers 4, 0, 10 don't and neither
                do the integers 1, 2, 2, 0. Similarly, the integers 1, 2, 3 don't form a peak because there
                aren't any strictly decreasing integers after the 3.

                Sample Input
                array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

                Sample Output
                6

"""

import unittest


def longest_peak(arr):
    max_peak_length = 0
    peaks = set()

    for i in range(1, len(arr) - 1):
        if is_peak(i, arr):
            peaks.add(i)

    for peak in peaks:
        left_bound = find_left_bound(peak, arr)
        right_bound = find_right_bound(peak, arr)
        length = right_bound - left_bound - 1
        max_peak_length = max(max_peak_length, length)

    return max_peak_length


def is_peak(index, arr):
    return arr[index] > arr[index - 1] and arr[index] > arr[index + 1]


def find_left_bound(index, arr):
    left_index = index - 2
    while left_index >= 0 and arr[left_index] < arr[left_index + 1]:
        left_index -= 1

    return left_index


def find_right_bound(index, arr):
    right_index = index + 2
    while right_index < len(arr) and arr[right_index] < arr[right_index - 1]:
        right_index += 1

    return right_index


class TestLongestPeak(unittest.TestCase):
    def test_input_array_has_valid_longest_peak(self):
        actual = longest_peak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3])
        expected = 6
        self.assertEqual(expected, actual)

    def test_input_array_has_invalid_longest_peak(self):
        actual = longest_peak([2, 3])
        expected = 0
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()