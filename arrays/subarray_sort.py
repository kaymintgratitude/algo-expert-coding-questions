"""
Problem:        Sub Array Sort
Description:    Write a function that takes in an array of at least two integers and that returns an array of the 
                starting and ending indices of the smallest subarray in the input array that needs to sorted in 
                place in order for the entire input array to be sorted (in ascending order).

                If the input array is already sorted the function should return [-1, -1]

                Sample Input
                array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]

                Sample Output
                [3, 9]

"""
import unittest


def subarray_sort(array):
    max_out_of_order = float("-inf")
    min_out_of_order = float("inf")

    for i in range(len(array)):
        if is_out_of_order(i, array):
            max_out_of_order = max(array[i], max_out_of_order)
            min_out_of_order = min(array[i], min_out_of_order)

    start = 0
    current_number = array[start]
    while min_out_of_order >= current_number:
        start += 1
        current_number = array[start]

    end = len(array) - 1
    current_number = array[end]
    while max_out_of_order < current_number:
        end -= 1
        current_number = array[end]

    if max_out_of_order == float("-inf") or min_out_of_order == float("inf"):
        return [-1, -1]

    return [start, end]


def is_out_of_order(index, array):
    if index == 0:
        return array[index] > array[index + 1]
    if index == len(array) - 1:
        return array[index] < array[index - 1]

    return array[index] < array[index - 1] or array[index] > array[index + 1]


class TestSubArraySort(unittest.TestCase):
    def test_input_array_has_valid_sub_array_sort(self):
        actual = subarray_sort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19])
        expected = [3, 9]
        self.assertListEqual(expected, actual)

    def test_input_array_has_invalid_sub_array_sort(self):
        actual = subarray_sort([])
        expected = [-1, -1]
        self.assertListEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()