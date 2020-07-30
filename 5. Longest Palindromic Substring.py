'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            tmp = self.getlongestPalindrome(i, i, s)
            if len(tmp) > len(res):
                res = tmp
            tmp = self.getlongestPalindrome(i, i + 1, s)
            if len(tmp) > len(res):
                res = tmp
        return res

    def getlongestPalindrome(self, l, r, s):
        while l >= 0 and r < len(s) and (s[l] == s[r]):
            l -= 1
            r += 1
        return s[l + 1:r]