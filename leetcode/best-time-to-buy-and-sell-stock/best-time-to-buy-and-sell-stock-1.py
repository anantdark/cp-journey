from typing import List

# Brute Solution (TLE)
# Time Complexity: O(N^2) | Space Complexity: O(1)
# The brute approach is to try all possible combinations of buying and selling, 
# and find the maximum profit.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > 0 and profit > max_profit:
                    max_profit = profit
        return max_profit

## 
        print(nums)
arr = [2, 7, 11, 15]
val = 9
k = Solution().maxProfit(arr)
print(k)
        
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
