'''this method is faster than 92.27% of Python3 online submission'''
'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#https://www.cnblogs.com/grandyang/p/4051715.html
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.Symetric(root.left, root.right)

    def Symetric(self, left, right):
        if left == None and right == None:
            return True
        if (not left and right) or (left and not right) or (left.val != right.val):
            return False
        return self.Symetric(left.left, right.right) and self.Symetric(left.right, right.left)

