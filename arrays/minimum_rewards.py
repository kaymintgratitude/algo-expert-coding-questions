"""
Problem:        Minimum Range
Description:    Imagine that you're a teacher who's just graded the final exam in a class. You have a list of student
                scores on the final exam in a particular order (not necessarily sorted), and you want to reward your
                students. You decide to do so fairly by giving them arbitrary rewards following two rules:

                    1) All students must receive at least one reward.

                    2) Any given student must receive strictly more rewards than an adjacent student (a student immediately
                    to the left or to the right) with a lower score and must receive strictly fewer rewards than an adjacent 
                    student with a higher score.

                Write a function that takes in a list of scores and returns the minimum number of rewards that you must 
                give out to students to satisfy the two rules.

                You can assume that all students have different scores; in other words, the scores are all unique.

                Sample Input: 
                arrayOne = [8, 4, 2, 1, 3, 6, 7, 9, 5]

                Sample Output:
                25

"""

import unittest


def minimum_rewards(arr):
    rewards_list = [1] * len(arr)

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            rewards_list[i] = rewards_list[i - 1] + 1
        else:
            j = i - 1
            while j >= 0 and arr[j] > arr[j + 1]:
                rewards_list[j] = max(rewards_list[j], rewards_list[j + 1] + 1)
                j -= 1

    return sum(rewards_list)


class TestLongestRange(unittest.TestCase):
    def test_input_array_has_valid_minimum_rewards(self):
        actual = minimum_rewards([8, 4, 2, 1, 3, 6, 7, 9, 5])
        expected = 25
        self.assertEqual(expected, actual)

    def test_input_array_has_invalid_minimum_rewards(self):
        actual = minimum_rewards([])
        expected = 0
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
