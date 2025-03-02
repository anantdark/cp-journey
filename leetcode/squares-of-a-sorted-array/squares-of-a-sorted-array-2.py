from typing import List

# Optimal solution
# Time O(n) | Space O(n)
# Instead of searching for pivot like in better approach, we can have two pointers at both ends and insert from largest to smallest.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [0]*len(nums)
        i = 0
        j = len(nums)-1
        k = j
        while i <= j and k >= 0:
            if abs(nums[i]) > nums[j]:
                value = nums[i]**2
                i += 1
            else:
                value = nums[j]**2
                j -= 1
            squares[k] = value
            k -= 1
        return squares
## 
        print(nums)
arr = [-2, -1, 0, 3, 6]
k = Solution().sortedSquares(arr)
print(k)
        
# https://leetcode.com/problems/squares-of-a-sorted-array/
