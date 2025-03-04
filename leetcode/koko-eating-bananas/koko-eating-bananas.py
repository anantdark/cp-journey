from typing import List
import math

# optimized solution
# Time O(logn) | Space O(1)
# https://leetcode.com/problems/koko-eating-bananas/solutions/769702/python-clear-explanation-powerful-ultimate-binary-search-template-solved-many-problems
# Read editorial

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        def find_eat_time(speed):
            hours = 0
            for bananas in piles:
                temp = math.ceil(bananas/speed)
                hours += temp
            return hours
        while start < end:
            mid = start + (end-start)//2
            eating_time = find_eat_time(speed = mid)
            if eating_time <= h:
                end = mid # koko can eat in same time for speed > mid
            else:
                start = mid + 1 # koko can't eat in same time for speed < mid
        return end

## 
        print(nums)
arr = [3,6,7,11]
h = 8
k = Solution().minEatingSpeed(arr, h)
print(k)
        
# https://leetcode.com/problems/koko-eating-bananas/
