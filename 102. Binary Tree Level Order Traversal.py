'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        res = []
        next_level = [root]
        while next_level:
            current_level = next_level
            next_level = []
            vals = []
            while current_level:
                ele = current_level.pop(0)
                vals.append(ele.val)
                if ele.left != None:
                    next_level.append(ele.left)
                if ele.right != None:
                    next_level.append(ele.right)
            res.append(vals)
        return res