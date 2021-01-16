'''
(This problem is an interactive problem.)

A row-sorted binary matrix means that all elements are 0 or 1 and each row of the matrix is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return the index (0-indexed) of the leftmost column with a 1 in it. If such an index does not exist, return -1.

You can't access the Binary Matrix directly. You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
BinaryMatrix.dimensions() returns the dimensions of the matrix as a list of 2 elements [rows, cols], which means the matrix is rows x cols.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes, the input will be the entire binary matrix mat. You will not have access to the binary matrix directly.
'''
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        [m,n] = binaryMatrix.dimensions()
        res = []
        for i in range(m):
            l = 0
            u = n-1
            mid = int((l+u)/2)
            if not binaryMatrix.get(i,u):
                continue
            elif binaryMatrix.get(i,0):
                 res.append(0)
            else:
                while l<mid:
                    if binaryMatrix.get(i,mid):
                        u = mid
                        mid = int((l+u)/2)
                    else:
                        l = mid
                        mid = int((l+u)/2)
                res.append(u)
        return min(res) if res else -1