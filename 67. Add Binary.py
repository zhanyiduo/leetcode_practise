'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        of = 0
        for i in range(1,max(len(a),len(b))+1):
            if i>len(a):
                cur = int(b[-i])+of
            elif i>len(b):
                cur = int(a[-i])+of
            else:
                cur = int(a[-i])+int(b[-i])+of
            if cur > 1:
                of = 1
                cur -= 2
            else:
                of = 0
            res += str(cur)
        if of:
            res += str(of)
        return res[::-1]