'''Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]


Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
Each element of candidate is unique.
1 <= target <= 500'''

class Solution:
    def combinationSum(self, candidates, target):
        sol = []
        for idx, val in enumerate(candidates):
            if val == target:
                sol.append([val])
            elif val < target:
                subsol = self.combinationSum(candidates,target-val)
                subsol = [[val]+x for x in subsol]
                for ele in subsol:
                    sol.append(ele)
            else:
                continue
        final_sol = []
        for idx,ele in enumerate(sol):
            ele.sort()
            if ele not in final_sol:
                final_sol.append(ele)
        return final_sol

sol = Solution()
res = sol.combinationSum([1,2,3],3)
print(res)