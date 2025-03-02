from typing import List

# Optimal Solution 
# Time complexity: O(logn) | Space complexity: O(1)
# In this solution we are binary search to find the smallest element. The pattern to catch here is that for the smallest element in rotated array, the left element will be larger than the current element, and if we are at the largest element, the right element will be smaller. In all other cases vice-versa will hold true. We have to keep traversing until we hit this inflection point(s).

class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums)-1
        mid = 0
        if nums[0] <= nums[-1]:
            # already in original rotated place
            return nums[0]
        while i <= j:
            mid = i + (j-i)//2
            if nums[mid] < nums[mid-1]:
                # if we are at inflection point
                return nums[mid]
            elif nums[mid] > nums[mid+1]:
                # if we are before inflection point
                return nums[mid+1]
            else:
                if nums[mid] > nums[i]:
                    i = mid + 1
                else:
                    j = mid - 1
        return nums[mid]

        ##
        print(nums)


arr = [-2, 0, -1]
k = Solution().findMin(arr)
print(k)

# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
