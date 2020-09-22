'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
'''


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        return max(self.rob_noncircle(nums[1:]),
                   self.rob_noncircle(nums[:-1]))  # get the max between giving up first and last

    def rob_noncircle(self, s):
        n = len(s)
        g = [0] * n
        if n <= 2:
            return max(s)
        g[0] = s[0]
        g[1] = max(s[1], g[0])
        for i in range(2, n):
            g[i] = max(s[i] + g[i - 2], g[i - 1])  # get the next item by comparing the largest
        return g[n - 1]