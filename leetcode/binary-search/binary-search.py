from typing import List

# optmized solution
# Time O(log n) | Space O(1)
# This is vanilla binary search implementation.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)-1
        mid = -1
        while i <= j:
            mid = i + (j-i)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return -1

## 
        print(nums)
arr = [2, 7, 11, 15]
a = 7
k = Solution().search(arr, a)
print(k)
        
# https://leetcode.com/problems/binary-search/
