'''Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)<1 or target == None:
            return [-1,-1]
        l = 0
        u = len(nums)-1
        while l<=u:
            if nums[l]<target:
                l += 1
            elif nums[u]>target:
                u -= 1
            else:
                return [l,u]
        return [-1,-1]