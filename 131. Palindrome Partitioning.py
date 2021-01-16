'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
        res = []
        for idx in range(len(s)):
            if not self.isPalidrome(s[:idx + 1]):
                continue
            rest_pali_list = self.partition(s[idx + 1:])
            for ele in rest_pali_list:
                ele.insert(0, s[:idx + 1])
                res.append(ele)
        return res

    def isPalidrome(self, s):
        low = 0
        high = len(s) - 1
        while low < high:
            if s[low] != s[high]:
                return False
            else:
                low += 1
                high -= 1
        return True
