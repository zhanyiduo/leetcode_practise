'''A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] or obstacleGrid[m-1][n-1]:
            return 0
        d = [[0]*n for i in range(m)]
        d[0][0] = 1
        for i in range(1,m): #iterate 1st col
            if not obstacleGrid[i][0]:
                d[i][0] = d[i-1][0]
        for j in range(1,n):
            if not obstacleGrid[0][j]:
                d[0][j] = d[0][j-1]
        for i in range(1,m):
            for j in range(1,n):
                if not obstacleGrid[i][j]:
                    d[i][j] = d[i-1][j] + d[i][j-1]
        return d[m-1][n-1]