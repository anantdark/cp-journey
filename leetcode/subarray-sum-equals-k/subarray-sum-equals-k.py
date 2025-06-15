from typing import List
from collections import defaultdict

# Optimized solution
# Time O(N) | Space O(N)
# https://www.youtube.com/watch?v=KDH4mhFVvHw

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum, counter, sum_freq = 0, 0, defaultdict(int)
        for num in nums:
            prefix_sum += num
            remain = prefix_sum - k
            if remain == 0:
                counter += 1
            counter += sum_freq[remain]
            sum_freq[prefix_sum] += 1
        return counter

## 
        print(nums)
arr = [1,-1,0]
val = 0
k = Solution().subarraySum(arr, val)
print(k)
        
# https://leetcode.com/problems/subarray-sum-equals-k/
