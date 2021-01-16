'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
'''
#similar to the level triversal
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        next_level = [root]
        while next_level:
            cur_level = next_level
            next_level = []
            cur_val = []
            for ele in cur_level:
                if ele.left:
                    next_level.append(ele.left)
                if ele.right:
                    next_level.append(ele.right)
                cur_val.append(ele.val)
            res.append(cur_val[-1])
        return res