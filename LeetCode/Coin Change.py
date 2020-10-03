"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the
fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
Example 4:

Input: coins = [1], amount = 1
Output: 1
Example 5:

Input: coins = [1], amount = 2
Output: 2
"""

import sys
class Solution:
    def coinChange(self, coins, amount):
        sorted(coins)
        if amount == 0:
            return 0
        f = [sys.maxsize] * (amount+1)
        f[0]=0
        # coin denominations will be set as 1
        for x in coins:
            if x >= len(f):
                break
            f[x] = 1
        for a in range(0, amount+1, 1):
            min_val = sys.maxsize
            for x in coins:
                if a-x < 0:
                    continue
                if min_val > (f[a-x]+1):
                    min_val = f[a-x] + 1
                # min_val = min(min_val, f[a-x] + 1)
            if f[a] > min_val:
                f[a] = min_val
            # f[a] = min(min_val, f[a])
        if f[amount] == sys.maxsize:
            f[amount] = -1
        return f[amount]

coins = [2147483647]
amount = 1
print(Solution().coinChange(coins, amount))
