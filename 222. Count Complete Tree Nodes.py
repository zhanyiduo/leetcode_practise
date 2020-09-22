'''
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input:
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
'''
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        next_level = [root]
        res = 0
        level = 0
        while next_level:
            current_level = next_level
            res += len(current_level)
            next_level = []
            while current_level:
                ele = current_level.pop(0)
                if ele.left != None:
                    next_level.append(ele.left)
                if ele.right !=None:
                    next_level.append(ele.right)
        return res