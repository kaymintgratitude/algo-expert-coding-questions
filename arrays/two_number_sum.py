"""
Problem:        Two Number Sum
Description:    Write a function that take in a non-empty array of distinct integers and an integer
                representing a target sum. If any two numbers in the input array sum up to the target sum,
                the function should them in an array, in any order. If no two numbers sum up to the target sum,
                the function should return an empty array. 

                Note that the target sum has to be obtained by summing two different integers in the array; you 
                can't add a single integer to itself to obtain the target sum. 

                You can assume that there will be at most one pair of numbers summing up to the target sum.

                Sample Input: 
                array = [ 3, 5, -4, 8, 11, 1, -1, 6]
                targetSum = 10

                Sample Output:
                [-1, 11]
               
"""
import unittest


def two_number_sum(arr, targetSum):
    '''
    Time Complexity: O(n)
    Space Complexity: O(1)
    '''
    dedup_set = set()
    for currentNum in arr:
        difference = targetSum - currentNum
        if difference in dedup_set:
            return [ difference, currentNum]
        dedup_set.add(currentNum)
    
    return []


class TestTwoNumberSum(unittest.TestCase):
    
    def test_input_array_has_valid_two_number_sum(self):
        actual = two_number_sum([ 3, 5, -4, 8, 11, 1, -1, 6], 10)
        expected = [11, -1]
        self.assertEqual(expected, actual)

    def test_input_array_has_invalid_two_number_sum(self):
        actual = two_number_sum([], 10)
        expected = []
        self.assertEqual(expected, actual)     



if __name__ == "__main__":
    unittest.main()

