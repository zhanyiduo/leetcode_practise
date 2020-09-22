'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if self.search(board, i, j, word, 0, visited):
                    return True
        return False

    def search(self, board, i, j, word, idx, visited):
        if idx >= len(word):
            return True
        m = len(board)
        n = len(board[0])
        if i < 0 or j < 0 or i >= m or j >= n or visited[i][j] or board[i][j] != word[idx]:
            return False
        visited[i][j] = 1
        res = self.search(board, i + 1, j, word, idx + 1, visited) or \
              self.search(board, i, j + 1, word, idx + 1, visited) or \
              self.search(board, i - 1, j, word, idx + 1, visited) or \
              self.search(board, i, j - 1, word, idx + 1, visited)
        visited[i][j] = 0
        return res