'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = 10000
        clt = 10000
        nums.sort()
        for i in range(0, len(nums) - 2):
            l = i + 1
            u = len(nums) - 1
            while l < u:
                s = nums[i] + nums[l] + nums[u]
                if s == target:
                    return s
                elif s < target:
                    l += 1
                else:
                    u -= 1

                if abs(s - target) < diff:
                    clt = s
                    diff = abs(s - target)
        return clt
