'''
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''

################DFS################
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        self.visited = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0' or self.visited[i][j]:
                    continue
                self.traversal_island(grid,i,j,m,n)
                res += 1
        return res
    def traversal_island(self,grid,i,j,m,n):
        if i<0 or i>=m or j<0 or j>=n or self.visited[i][j] or grid[i][j]=='0':
            return
        self.visited[i][j] = 1
        self.traversal_island(grid,i-1,j,m,n)
        self.traversal_island(grid,i+1,j,m,n)
        self.traversal_island(grid,i,j-1,m,n)
        self.traversal_island(grid,i,j+1,m,n)
############BFS#####################
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        visited = [[0] * n for i in range(m)]
        dirx = [1, -1, 0, 0]
        diry = [0, 0, 1, -1]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0' or visited[i][j]:
                    continue
                res += 1
                visited[i][j] = 1
                queue = [(i, j)]
                while queue:
                    (x0, y0) = queue.pop(0)
                    # traversal its neigbor
                    for k in range(4):
                        x = x0 + dirx[k]
                        y = y0 + diry[k]
                        if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or grid[x][y] == '0':
                            continue
                        queue.append((x, y))
                        visited[x][y] = 1

        return res
