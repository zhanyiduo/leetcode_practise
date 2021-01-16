'''
Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.



Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5


Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
'''
# https://www.cnblogs.com/grandyang/p/4601208.html

'''
The idea is to use stack record each number. If the operator is product before the number, then pop the last stack number to opearte with the current number
'''


class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        nums = []
        ops = '+'
        cur = []
        s = s + '+'
        for idx, ele in enumerate(s):
            if ele not in ['+', '-', '*', '/']:
                cur.append(ele)
            else:
                num = int("".join(cur))
                if ops == '+':
                    nums.append(num)
                elif ops == '-':
                    nums.append(-num)
                elif ops == '*':
                    num *= nums.pop()
                    nums.append(num)
                else:
                    last = nums.pop()
                    num = int(last / num)
                    nums.append(num)
                ops = ele
                cur = []

        return sum(nums)
