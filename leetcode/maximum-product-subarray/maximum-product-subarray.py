from typing import List

# Optimal Solution 
# Time complexity: O(n) | Space complexity: O(1)
# In this solution we are using modified kadane algorithm, we are traversing the array and keeping track of max and min both because min can turn into max if multiplied by another negative number, so for each current value we calculate the max and min from (current, max*current, min*current), this also refreshes if there is 0 in between because then all values will be 0.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_so_far = nums[0]
        min_so_far = nums[0]
        final_max = nums[0]
        for i in range(1, len(nums)):
            current = nums[i]
            temp_max = max(current, max(current*max_so_far, current*min_so_far))
            min_so_far = min(current, min(current*max_so_far, current*min_so_far))
            max_so_far = temp_max
            if final_max < max_so_far:
                final_max = max_so_far
        return final_max



        ##
        print(nums)


arr = [-2, 0, -1]
k = Solution().maxProduct(arr)
print(k)

# https://leetcode.com/problems/maximum-product-subarray/
