from typing import List

# Better solution
# Time O(n) | Space O(n)
# We are searching linearly for the pivot where negative number ends, from there we use two pointers one traverses forward another backward and square of smaller element gets added to final list.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = []
        i = 0
        j = -1
        if (nums[0] < 0):
            if nums[-1] < 0:
                i = len(nums)
                j = len(nums)-1
            else:
                while nums[i] < 0:
                    i += 1
                    continue
                j = i-1
        
            while i < len(nums) and j >= 0:
                if -nums[j] < nums[i]:
                    squares.append(nums[j]**2)
                    j -= 1
                else:
                    squares.append(nums[i]**2)
                    i += 1
        while i < len(nums):
            squares.append(nums[i]**2)
            i += 1
        while j >= 0:
            squares.append(nums[j]**2)
            j -= 1
        return squares

## 
        print(nums)
arr = [-2, -1, 0, 3, 6]
k = Solution().sortedSquares(arr)
print(k)
        
# https://leetcode.com/problems/squares-of-a-sorted-array/
