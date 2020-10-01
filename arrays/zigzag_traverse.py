"""
Problem:        Zigzag Traverse
Description:    Write a function that takes in an n x m two-dimensional array (that can be square-shaped when n==m)
                and returns a one-dimensional array of all the array's elements in zigzag order.

                Zigzag order starts at the top left corner of the two-dimensional array, goes down by one element and 
                proceeds in a zig zag pattern all the way to the bottom of the right corner

                Sample Input: 
                arrayOne = [
                        [1, 3, 4, 10],
                        [2, 5, 9, 11],
                        [6, 8, 12, 15],
                        [7, 13, 14, 16]
                    ]

                Sample Output:
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

"""

import unittest


def zigzag_traverse(arr):
    def is_out_of_bounds(row, col, height, width):
        return row < 0 or col < 0 or col > width or row > height

    row, col = 0, 0
    height, width = len(arr) - 1, len(arr[0]) - 1
    result = []
    going_down = True

    while not is_out_of_bounds(row, col, height, width):
        result.append(arr[row][col])
        if going_down:
            if col == 0 or row == height:
                going_down = False
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if row == 0 or col == height:
                going_down = True
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1

    return result


class TestZigzagTraverse(unittest.TestCase):
    def test_input_array_has_valid_zigzag_traverse(self):
        input_array = [[1, 3, 4, 10], [2, 5, 9, 11], [6, 8, 12, 15], [7, 13, 14, 16]]
        actual = zigzag_traverse(input_array)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self.assertListEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()