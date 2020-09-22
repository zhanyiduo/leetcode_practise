'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        next_level = [root]
        res = []
        rev = 0
        while next_level:
            current_level = next_level
            next_level = []
            temp = []
            for ele in current_level:
                temp.append(ele.val)
                if ele.left != None:
                    next_level.append(ele.left)
                if ele.right != None:
                    next_level.append(ele.right)
            if rev:
                res.append(temp[::-1])
                rev = 0
            else:
                res.append(temp)
                rev = 1
        return res