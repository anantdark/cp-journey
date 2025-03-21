from typing import List

# Optimal Solution (TLE)
# Time complexity: O(n) | Space complexity: O(1)
# For optimal approach we are using Kadane's Algorithm, in this approach we are traversing the array in single pass and started to make max subarray, every new element we encounter is also considered it's own subarray, if our current max subarray is < 0 then we wait for a positive value since negative numbers reduce total sum, and assign the first positive number as our max subarray.
# But if our current max subarray is > 0, then we are updating our max subarray with the current max subarray + the current element.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = int(-1e5)
        current_sum = 0
        for i in nums:
            current_sum += i
            if max_sum < current_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0
        return max_sum
            

        ##
        print(nums)


arr = [5, 4, -1, 7, 8]
k = Solution().maxSubArray(arr)
print(k)

# https://leetcode.com/problems/maximum-subarray/
