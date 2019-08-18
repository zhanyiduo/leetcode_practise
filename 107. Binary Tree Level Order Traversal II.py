'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        self.listTree = []
        level = 0
        if root != None:
            self.add_node(root,level)
        return self.listTree[::-1]
    def add_node(self, root, level):
        if len(self.listTree)<level+1:
            self.listTree.append([root.val])
        else:
            self.listTree[level].append(root.val)
        level += 1
        if root.left != None:
            self.add_node(root.left,level)
        if root.right != None:
            self.add_node(root.right,level)
        return None