'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


Constraints:

1 <= n <= 19
'''
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0 or n==1:
            return 1
        res = 0
        for i in range(1,n+1):
            n_l = i-1 #how many numbers should go to its left nodes
            n_r = n-i #how many numbers should go to its right nodes
            res = res+self.numTrees(n_l)*self.numTrees(n_r) #adding numbers of combinations from left and right
        return res