'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if target == None or len(nums) < 4:
            return []
        else:
            res = []
            nums.sort()
            i = 0
            while i < len(nums):
                j = i + 1
                while j < len(nums):
                    l = j + 1
                    u = len(nums) - 1
                    while l < u:
                        s = nums[i] + nums[j] + nums[l] + nums[u]
                        if s == target:
                            res.append([nums[i], nums[j], nums[l], nums[u]])
                            l += 1
                            u -= 1
                            while (l < u) and (nums[l] == nums[l - 1]):  # remove duplicates on l
                                l += 1
                            while (l < u) and (nums[u] == nums[u + 1]):
                                u -= 1
                        elif s < target:
                            l += 1
                        else:
                            u -= 1
                    while (j < len(nums) - 1) and (nums[j] == nums[j + 1]):
                        j += 1
                    j += 1
                while (i < len(nums) - 1) and (nums[i] == nums[i + 1]):
                    i += 1
                i += 1
            return res
