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
#2020-08-09 solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        n = len(s)
        p = [[0]*n for i in range(n)]
        maxlen = 0
        res = ''
        for k in range(n-1):
            p[k][k] = 1
            i = k
            if s[i] == s[i+1]:#consider 2 next to each other
                j = i+1
                p[i][j] = 1
                while i-1>=0 and j+1<n:
                    if s[i-1] == s[j+1] and p[i][j]:
                        i-=1
                        j+=1
                        p[i][j]=1
                    else:
                        break
                if maxlen < j-i+1:
                    maxlen = j-i+1
                    res = s[i:j+1]
            #consider one centric case
            i = k
            j = k
            while i-1>=0 and j+1<n:
                if s[i-1] == s[j+1] and p[i][j]:
                    i-=1
                    j+=1
                    p[i][j]=1
                else:
                    break
            if maxlen < j-i+1:
                maxlen = j-i+1
                res = s[i:j+1]
        return res