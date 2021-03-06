'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<=1:
            return [nums]
        else:
            sol = []
            for i in nums:
                res = nums.copy()
                res.remove(i)
                SubPermuteList = self.permute(res)
                for list_j in SubPermuteList:
                    list_j.insert(0,i)
                    sol.append(list_j)
            return sol