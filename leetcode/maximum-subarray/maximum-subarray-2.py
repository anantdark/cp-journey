from typing import List

# Better Solution (TLE)
# Time complexity: O(n^2) | Space complexity: O(1)
# In this solution we are traversing the array and maintaining the arr_sum variable with the sum, thus reducing one for loop that calculated the sum each time.
# After that we are checking if the arr_sum is greater than the max_sum, then we are updating the max_sum variable with the arr_sum.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = int(-1e5)
        for i in range(len(nums)):
            arr_sum = 0
            for j in range(i, len(nums)):
                arr_sum += nums[j]
                if arr_sum > max_sum:
                    max_sum = arr_sum
        return max_sum


        ##
        print(nums)


arr = [5, 4, -1, 7, 8]
k = Solution().maxSubArray(arr)
print(k)

# https://leetcode.com/problems/maximum-subarray/
