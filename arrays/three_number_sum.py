"""
Problem:        Three Number Sum
Description:    Write a function that takes in a non-empty array of distinct integers and an integer representing
                a target sum. The function should find all triplets in the array that sum up to the target sum 
                and return a two dimensional array of all these triplets. The numbers in each triplet should be order
                in ascending order, and the triplets themselves should be ordered in ascending order with respect to the
                numbers they hold.

                If no three numbers sum up to the target sum, the function should return an empty array


                Sample input:
                array = [12, 3, 1, 2, -6, 5, -8, 6]
                targetSum = 0

                Sample Output:
                [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

"""

import unittest


def three_number_sum(arr, target_sum):
    """
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    arr.sort()
    triplets = []

    for current_index in range(len(arr) - 2):
        current_number = arr[current_index]
        left_pointer = current_index + 1
        right_pointer = len(arr) - 1

        while left_pointer < right_pointer:
            left, right = arr[left_pointer], arr[right_pointer]
            current_sum = current_number + left + right

            if current_sum == target_sum:
                triplets.append([current_number, left, right])
                left_pointer += 1
                right_pointer -= 1
            elif current_sum < target_sum:
                left_pointer += 1
            else:
                right_pointer -= 1

    return sorted(triplets, key=lambda x: x[0]) if triplets else triplets


class TestThreeNumberSum(unittest.TestCase):
    def test_input_array_has_valid_three_number_sum(self):
        actual = three_number_sum([12, 3, 1, 2, -6, 5, -8, 6], 0)
        expected = [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
        self.assertEqual(expected, actual)

    def test_input_array_has_invalid_three_number_sum(self):
        actual = three_number_sum([], 10)
        expected = []
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
