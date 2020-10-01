"""
Problem:        Longest range
Description:    Write a function that takes in an array of integers and returns an array of length  2 representing the
                largest range of integers contained in that array.

                The first number in the output array should be the first number in the range, while the second number
                number should be the last number in the range. 

                A range of is defined as a set of numbers that come right after each other in the set of real integers.
                For instance, the output array [2, 6] represents the {2, 3, 4, 5, 6}, which is a range of the length 5.
                Note that numbers don't need to be sorted or adjacent in the input array in order to form a range.

                You can assume that there will be only one largest range.

                Sample Input: 
                arrayOne = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]

                Sample Output:
                [0, 7]

"""

import unittest


def longest_range(arr):
    check_dict = {}
    max_range = []

    for num in arr:
        check_dict[num] = True

    for i, num in enumerate(arr):
        if check_dict[num]:
            current_range = [num]
            check_dict[num] = False
            next_less_num_in_range = num - 1

            while (
                next_less_num_in_range in check_dict
                and check_dict[next_less_num_in_range]
            ):
                current_range.insert(0, next_less_num_in_range)
                check_dict[next_less_num_in_range] = False
                next_less_num_in_range -= 1

            next_great_num_in_range = num + 1
            while (
                next_great_num_in_range in check_dict
                and check_dict[next_great_num_in_range]
            ):
                current_range.append(next_great_num_in_range)
                check_dict[next_great_num_in_range] = False
                next_great_num_in_range += 1

            if len(current_range) > len(max_range):
                max_range = current_range

    return [max_range[0], max_range[-1]] if max_range else []


class TestLongestRange(unittest.TestCase):
    def test_input_array_has_longest_range(self):
        actual = longest_range([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6])
        expected = [0, 7]
        self.assertEqual(expected, actual)

    def test_input_array_has_invalid_longest_range(self):
        actual = longest_range([])
        expected = []
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
