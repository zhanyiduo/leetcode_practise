'''
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:#reverse the preorder traversal
        if root == None:
            return []
        res = []
        stack = []
        current = root
        while stack or current != None:
            if current != None:
                stack.append(current)
                res.insert(0,current.val)
                current = current.right
            else:
                current = stack.pop()
                current = current.left
        return res