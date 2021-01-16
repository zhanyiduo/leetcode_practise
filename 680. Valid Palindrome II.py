'''
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        u = len(s)-1
        while l<u:
            if s[l] == s[u]:
                l+=1
                u-=1
            else:
                temp1 = s[l+1:u+1] #skip l
                temp2 = s[l:u] #skip u
                return temp1==temp1[::-1] or temp2==temp2[::-1]
        return True