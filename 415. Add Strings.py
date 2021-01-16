'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        adv = 0
        sumlist = []
        l1 = list(num1[:])
        l2 = list(num2[:])
        while l1 or l2:
            cur1 = l1.pop() if l1 else 0
            cur2 = l2.pop() if l2 else 0
            cum = int(cur1) + int(cur2) + adv
            print(cum)
            if cum >= 10:
                cum -= 10
                adv = 1
            else:
                adv = 0
            sumlist.insert(0, str(cum))
        if adv:
            sumlist.insert(0, str(adv))
        return "".join(sumlist)
