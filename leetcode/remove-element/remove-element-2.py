from typing import List

# Optimized solution - 1
# Time O(N) | Space O(1)
# In previous solution we are moving all values not equal to num, if num count is less we are performing many unnecessary operations, we can instead use pointer on both ends and move pointer at 0 swapping indexes with val with end pointer.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums)
        while i < j:
            if nums[i] == val:
                nums[i] = nums[j-1]
                j -= 1
            else:
                i += 1
        return j

## 
        print(nums)
arr = [9, 2, 2, 9]
val = 9
k = Solution().removeElement(arr, 9)
print(k)
        
# https://leetcode.com/problems/remove-element/
