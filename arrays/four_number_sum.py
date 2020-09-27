"""
Problem:        Four Number Sum
Description:    Write a function that takes in a non-empty array of distinct integers and an integer 
                representing a target sum. The function should find all quadruplets in the array that
                sum up to the target sum and return a two-dimensional array of all these quadruplets
                in no particular order.

                If no four numbers sum up to the target sum, the function should return an empty array.

                Sample Input
                array = [7, 6, 4, -1, 1, 2]
                targetSum = 16

                Sample Output
                [[7, 6, 4, -1], [7, 6, 1, 2]]

"""

import unittest


def four_number_sum(arr, target_sum):
    """
    Time Complexity: Avg: O(n^2) Worst O(n^3)
    Space Complexity: O(n^2)
    """
    all_pairs_sum = {}
    quadruplets = []
    for i in range(1, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            current_sum = arr[i] + arr[j]
            difference = target_sum - current_sum
            if difference in all_pairs_sum:
                for pair in all_pairs_sum[difference]:
                    quadruplets.append(pair + [arr[i], arr[j]])
        for k in range(0, i):
            q = arr[i] + arr[k]
            if q not in all_pairs_sum:
                all_pairs_sum[q] = [[arr[k], arr[i]]]
            else:
                all_pairs_sum[q].append([arr[k], arr[i]])

    return quadruplets


class TestSmallestDifference(unittest.TestCase):
    def test_input_array_has_valid_four_number_sum(self):
        actual = four_number_sum([7, 6, 4, -1, 1, 2], 16)
        expected = [[7, 6, 4, -1], [7, 6, 1, 2]]
        self.assertListEqual(expected, actual)

    def test_input_array_has_invalid_four_number_sum(self):
        actual = four_number_sum([], 10)
        expected = []
        self.assertListEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()