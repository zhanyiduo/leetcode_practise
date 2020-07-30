'''Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]'''
class Solution:
    def combinationSum2(self, candidates, target):
        self.sol = []
        candidates.sort()
        current = []
        self.getcombsum(candidates,target,current)
        return self.sol
    def getcombsum(self,candidates,target,current):
        if target == 0:
            self.sol.append(current)
        if target < 0:
            return None
        else:
            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                self.getcombsum(candidates[i+1:],target-candidates[i],current+[candidates[i]])