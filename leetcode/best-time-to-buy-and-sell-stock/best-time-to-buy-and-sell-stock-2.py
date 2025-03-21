from typing import List

# Optimal Solution
# Time Complexity : O(n) | Space Complexity : O(1)
# The optimal solution is to use two pointers to solve the problem. While traversing the array we update the min_value whenever we see the lowest price, this will give us the lowest price until now, then the profit calculated from that will be optimal, if it is greater than the max_profit until now, we update it.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_value = int(1e5)
        for price in prices:
            if price < min_value:
                min_value = price

            profit = price - min_value
            if profit > max_profit:
                max_profit = profit
        return max_profit

## 
        print(nums)
arr = [2, 7, 11, 15]
val = 9
k = Solution().maxProfit(arr)
print(k)
        
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
