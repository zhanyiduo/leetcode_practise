'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        last_sum = [triangle[0][0]]
        for k in range(1,len(triangle)):
            current_sum = [0]*len(triangle[k])
            for idx,val in enumerate(triangle[k]):
                if idx==0:
                    current_sum[idx] = val+last_sum[idx]
                elif idx == len(triangle[k])-1:
                    current_sum[idx] = val+last_sum[idx-1]
                else:
                    current_sum[idx] = val+min(last_sum[idx],last_sum[idx-1])
            last_sum = current_sum.copy()
        return min(last_sum)