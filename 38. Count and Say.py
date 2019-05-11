'''
terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.
'''
class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        else:
            out_str = {}
            out_str[0] = '1'
            for k in range(1,n):
                count = 0
                cur_str = ""
                last = out_str[k-1][0]
                for i in out_str[k-1]:
                    if last == i:
                        count += 1
                        continue
                    else:
                        cur_str += str(count)+str(last)
                        last = i
                        count = 1
                cur_str += str(count)+str(last)
                out_str[k] = cur_str
            return cur_str