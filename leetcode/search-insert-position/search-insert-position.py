from typing import List

# optimized solution
# Time O(logn) | Space O(1)
# Binary search for element and if not found then if mid value is less than target then target will come after it so target index will be mid + 1, but if the value at mid is greater than target then target will come at mid position, so return mid.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)-1
        mid = 0
        while i <= j:
            mid = i + (j-i)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return mid + 1 if nums[mid] < target else mid

## 
        print(nums)
arr = [1, 3]
a = 2
k = Solution().searchInsert(arr, a)
print(k)
        
# https://leetcode.com/problems/search-insert-position/
