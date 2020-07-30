'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        threelist = []
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            u = len(nums) - 1
            while l < u:
                s = nums[l] + nums[u] + nums[i]
                if s > 0:
                    u -= 1
                elif s < 0:
                    l += 1
                else:
                    threelist.append([nums[i], nums[l], nums[u]])
                    l += 1
                    u -= 1
                    while l < u and nums[u] == nums[u + 1]:
                        u -= 1
                    while l < u and nums[l] == nums[l - 1]:
                        l += 1
        return threelist