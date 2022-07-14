'''
303. Range Sum Query - Immutable

Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
'''

class NumArray:
    '''
    [-2, 0, 3, -5, 2, -1]
    prefx_sums = [0, -2, -2, 1, -4, -2, -3]
    '''
    def __init__(self, nums: list[int]):
        self.prefix_sums = [0] + nums
        for i in range(1, len(self.prefix_sums)):
            self.prefix_sums[i] = self.prefix_sums[i] + self.prefix_sums[i - 1]
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sums[right + 1] - self.prefix_sums[left]
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# Unit Test
import unittest
class TestNumArray(unittest.TestCase):
    def testNumArray1(self):
        numArray = NumArray([-2, 0, 3, -5, 2, -1])
        self.assertAlmostEqual(numArray.sumRange(0, 2), 1)
        self.assertAlmostEqual(numArray.sumRange(2, 5), -1)
        self.assertAlmostEqual(numArray.sumRange(0, 5), -3)

if __name__ == '__main__':
    unittest.main()