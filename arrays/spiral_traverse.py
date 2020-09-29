"""
Problem:        Spiral Traverse
Description:    Write a function that takes in an n x m two-dimensional array (that can be square-shaped when 
                n==m) and returns a one-dimensional array of all the array's elements in spiral order.

                Spiral order start at the top left corner of the two-dimensional array, goes to the right, and proceeds 
                in a spiral pattern all the way until every element has been visited.

                Sample Input
                array = [
                    [1, 2, 3, 4],
                    [12, 13, 14, 5],
                    [11, 16, 15, 6],
                    [10, 9, 8, 7]
                ]

                Sample Output
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

"""

import unittest


def spiral_traverse(arr):
    result = []
    start_col, end_col = 0, len(arr[0]) - 1
    start_row, end_row = 0, len(arr) - 1
    while start_row <= end_row and start_col <= end_col:

        # go right
        for col in range(start_col, end_col + 1):
            result.append(arr[start_row][col])

        # go down
        for row in range(start_row + 1, end_row + 1):
            result.append(arr[row][end_col])

        # go left
        for col in reversed(range(start_col, end_col)):
            if start_row == end_row:
                break
            result.append(arr[end_row][col])

        # go up
        for row in reversed(range(start_row + 1, end_row)):
            if start_col == end_col:
                break
            result.append(arr[row][start_col])

        start_col += 1
        end_col -= 1
        start_row += 1
        end_row -= 1

    return result


class TestSpiralTraverse(unittest.TestCase):
    def test_input_array_has_valid_spiral_traverse(self):
        input_array = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
        actual = spiral_traverse(input_array)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()