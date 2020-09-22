'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
'''

##https://www.cnblogs.com/grandyang/p/5138186.html
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0

        s = [amount + 1] * (amount + 1)  # s:number of coins needed for amount i, initialize with largest value
        s[0] = 0
        for i in range(amount + 1):
            for j in range(len(coins)):
                if i >= coins[j]:
                    s[i] = min(s[i], s[i - coins[j]] + 1)

        return -1 if s[-1] > amount else s[-1]