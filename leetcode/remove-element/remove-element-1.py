from typing import List

# Optimized solution - 1
# Time O(N) | Space O(1)
# In this problem, we are moving two pointers i and j from position 0, i is swapping all the elements that are not equal to value with the element at the j pointer, and j is moving sequentially.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j

## 
        print(nums)
arr = [9, 2, 2, 9]
val = 9
k = Solution().removeElement(arr, 9)
print(k)
        
# https://leetcode.com/problems/remove-element/
