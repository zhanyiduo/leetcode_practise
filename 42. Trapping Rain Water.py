'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.



Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9


Constraints:

n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        vol = 0
        stack = []
        for idx, cur in enumerate(height):
            while stack and cur>height[stack[-1]]:
                bottom_idx = stack.pop() #bottom is the stack top
                bottom = height[bottom_idx]
                if not stack: #if this is no element left in the stack break
                    break
                lb_idx = stack[-1] #left bound is the current stack top
                elev = min(cur,height[lb_idx])-bottom #compute the height of water
                width = idx-lb_idx-1
                vol += elev*width
            stack.append(idx)
        return vol