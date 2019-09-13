'''\Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        tree = []
        tree.append([1])
        tree.append([1,1])
        def getnext(row,k):
            rowk = [1]
            for i in range(1,k):
                rowk.append(row[i-1]+row[i])
            rowk.append(1)
            return rowk
        for k in range(2,numRows):
            temp = getnext(tree[k-1],k)
            tree.append(temp)
        return tree