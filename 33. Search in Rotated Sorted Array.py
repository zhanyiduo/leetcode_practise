'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        l = 0
        u = len(nums) - 1
        m = int((l + u) / 2)
        while l < u:
            if target == nums[m]:
                return m
            elif target == nums[l]:
                return l
            elif target == nums[u]:
                return u

            if nums[l] < nums[u]:
                if target < nums[l] or target > nums[u]:
                    return -1
                elif target < nums[m]:
                    u = m
                    m = int((l + u) / 2)
                    continue
                else:
                    l = m + 1
                    m = int((l + u) / 2)
                    continue

            else:  # nums[l]>nums[u]
                if target < nums[l] and target > nums[u]:
                    return -1
                if nums[m] < nums[u]:
                    if target > nums[m] and target < nums[u]:
                        l = m + 1
                        m = int((l + u) / 2)
                        continue
                    else:  # target > nums[l] or target < nums[m]:
                        u = m
                        m = int((l + u) / 2)
                        continue
                else:  # nums[m]>=nums[l]
                    if target > nums[l] and target < nums[m]:
                        u = m
                        m = int((l + u) / 2)
                        continue
                    else:
                        l = m + 1
                        m = int((l + u) / 2)
                        continue

        if target == nums[l]:
            return l
        else:
            return -1