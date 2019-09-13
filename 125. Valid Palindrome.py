'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alpha = "".join(x for x in s if x.isalnum() )
        s_lower = s_alpha.lower()
        #s_half = s_lower[:int(len(s_lower)/2)]
        #s_rev = s_lower[:-int(len(s_lower)/2)-1:-1]
        return s_lower == s_lower[::-1]