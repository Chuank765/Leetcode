'''
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''

import unittest
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        TC:O(n)
        SC:O(n)
        '''
        nums_index = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums_index:
                return [i, nums_index[diff]]
            else:
                nums_index[num] = i

funcs = [Solution().twoSum]

class TestTwoSum(unittest.TestCase):
    def testTwoSum1(self):
        for func in funcs:
            self.assertEqual(sorted(func(nums=[2,7,11,15], target=9)), sorted([1, 0]))
    def testTwoSum2(self):
        for func in funcs:
            self.assertEqual(sorted(func(nums=[3, 2, 4], target=6)), sorted([1, 2]))
    def testTwoSum3(self):
        for func in funcs:
            self.assertEqual(sorted(func(nums=[3, 3], target=6)), sorted([0, 1]))

if __name__ == '__main__':
    unittest.main()