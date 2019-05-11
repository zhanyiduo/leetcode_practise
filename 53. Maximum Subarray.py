'''
Given an integer array nums,
find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_a = nums[0]
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            if temp > sum_a:
                sum_a = temp
            if temp < 0:
                temp = 0
        return sum_a
