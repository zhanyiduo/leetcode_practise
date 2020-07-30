'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l ,r = 0,len(height)-1
        lb ,ub = 0,len(height)-1
        maxcap = min(height[0],height[-1])*(len(height)-1)
        while l < r:
            if height[l]<height[r]:
                curcap = height[l]*(r-l)
                l += 1
            else:
                curcap = height[r]*(r-l)
                r -=1
            if curcap>maxcap:
                maxcap = curcap
        return maxcap