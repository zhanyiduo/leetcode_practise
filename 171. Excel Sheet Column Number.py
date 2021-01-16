'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
'''
class Solution:
    def titleToNumber(self, s: str) -> int:
        val = 0
        n = len(s)
        s_rev = s[::-1]
        for i in range(n):
            val += pow(26,i)*(ord(s_rev[i]) - ord('A') + 1)
        return val