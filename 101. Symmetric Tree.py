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

class Solution:
    # self.treelist = []
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        else:
            self.treelist = []
            level = 0
            self.getrootlist(root, level)
            print(self.treelist)
            for l in range(len(self.treelist)):
                if not self.islistsymmetry(self.treelist[l]):
                    return False
            return True

    def getrootlist(self, root, level):
        if len(self.treelist) < level + 1:
            self.treelist.append([root.val])
        else:
            self.treelist[level].append(root.val)
        level += 1
        if root.right:
            self.getrootlist(root.right, level)
        elif len(self.treelist) < level + 1:
            self.treelist.append([-999])
        else:
            self.treelist[level].append(-999)
        if root.left:
            self.getrootlist(root.left, level)
        elif len(self.treelist) < level + 1:
            self.treelist.append([-999])
        else:
            self.treelist[level].append(-999)

    def islistsymmetry(self, L):
        if (not L) or (len(L) == 1):
            return True
        else:
            for i in range(len(L)):
                if not (L[i] == L[-i - 1]):
                    return False
            return True