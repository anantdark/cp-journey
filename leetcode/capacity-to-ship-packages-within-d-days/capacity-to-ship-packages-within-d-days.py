from typing import List

# Optmized solution
# Time O(logN) | Space O(1)
# We are using binary search to find the minimum capacity to ship all the packages in the given days. The find_days function will return the number of days needed to ship all the packages.

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def find_days(weights, capacity):
            day_count = 1
            daily_load = 0
            for weight in weights:
                if daily_load + weight <= capacity:
                    daily_load += weight
                    continue
                daily_load = weight 
                day_count += 1
            return day_count
        
        max_cap = sum(weights)
        lo = max(weights)
        hi = max_cap
        mid = (lo+hi)//2
        while lo <= hi:
            mid = (lo + hi)//2
            days_needed = find_days(weights, mid)
            if days_needed <= days:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
        

        

## 
        # print(nums)
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
val = 5 
k = Solution().shipWithinDays(arr, val)
print(k)
        
# https://leetcode.com/problems/shipWithinDays/
