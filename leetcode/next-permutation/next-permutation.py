from typing import List, Optional

# Optimal solution
# Time O(N) | Space O(1)
# https://www.youtube.com/watch?v=JDOXKqF60RQ

class Solution:
    def nextPermutation(self, nums: List[int]):
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1

        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                index = i-1
                break 
        
        if index == -1:
            nums = nums.reverse()
            return nums
        
        for i in range(len(nums)-1, index, -1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                break #break out after first swap
        
        nums[index+1:] = sorted(nums[index+1:])
        return nums

## 
        print(nums)
arr = [1, 3, 2]
k = Solution().nextPermutation(arr)
print(k)
        
# https://leetcode.com/problems/next-permutation/
