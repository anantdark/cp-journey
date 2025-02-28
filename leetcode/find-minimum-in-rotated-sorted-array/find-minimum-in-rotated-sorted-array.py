from typing import List

# Optimal Solution 
# Time complexity: O(logn) | Space complexity: O(1)
# In this solution we are binary search to find the smallest element. The pattern to catch here is that if an array is not rotated from original position, for each of its elements the right element will be bigger and the left element smaller. But for a rotated array, the smallest element will be covered with both elements bigger than it. 

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            # array already sorted
            return nums[0]

        i, j = 0, len(nums)-1
        mid_index = 0
        while i < j:
            mid_index = (i+j+1)//2
            if nums[mid_index] <= nums[i] and nums[mid_index] >= nums[j]:
                return nums[mid_index]
            if nums[mid_index] > nums[i]:
                i = mid_index
            elif nums[mid_index] < nums[i]:
                j = mid_index
        return nums[mid_index]



        ##
        print(nums)


arr = [-2, 0, -1]
k = Solution().findMin(arr)
print(k)

# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
