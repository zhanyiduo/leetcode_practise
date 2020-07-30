'''Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]'''
class Solution:
    def generateMatrix(self,n):
        if n<=0:
            return None
        if n == 1:
            return [[n]]
        sol = []
        sol.append([x for x in range(1,n+1)])#include the first row
        subsol = self.generateMatrix(n-2)
        for i in range(1,n-1):
            sol.append([])
            incre_subsol = [x+n*n-(n-2)*(n-2) for x in subsol[i-1]]
            sol[i] = [n*n-(n-2)*(n-2)-i+1] + incre_subsol + [n+i]
        sol.append([x for x in range(3*n-2,2*n-2,-1)])
        return sol

test = Solution()
print(test.generateMatrix(5))