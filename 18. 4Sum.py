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
        #create two index i, j to go over the entire array. Then use two pointers l,u to find the residual
        if len(nums)<4:
            return []
        else:
            nums.sort()
            n = len(nums)
            sol = []
            for i in range(n-3):
                for j in range(i+1,n-2):
                    l = j+1
                    u = n-1
                    while l<u:
                        res = nums[i] + nums[j] + nums[l] + nums[u]
                        if res == target:
                            if [nums[i],nums[j],nums[l],nums[u]] not in sol:
                                sol.append([nums[i],nums[j],nums[l],nums[u]])
                            l += 1
                            u -= 1
                        elif res < target:
                            l +=1
                        else:
                            u -=1
            return sol
