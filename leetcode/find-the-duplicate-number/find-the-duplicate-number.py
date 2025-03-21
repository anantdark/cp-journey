from typing import List

# -- Constraints
# - Don't modify the array
# - Use only O(1) extra space

# Optmized solution
# Time O(n) | Space O(n)
# In this approach, we use the tortoise and hare algorithm to find the duplicate. The hare moves twice as fast as the tortoise. When the tortoise and the hare collide, the duplicate is found. 

class Solution:
    @staticmethod
    def move_n_index(nums, var, times):
        while times:
            var = nums[var]
            times -= 1
        return var

    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = 0
        hare = 0
        while tortoise != hare or tortoise == 0:
            hare = self.move_n_index(nums, hare, 2)
            tortoise = self.move_n_index(nums, tortoise, 1)
        
        hare = 0
        while tortoise != hare:
            hare = self.move_n_index(nums, hare, 1)
            tortoise = self.move_n_index(nums, tortoise, 1)
        
        return nums[hare]
        

## 
        print(nums)
arr = [3, 1, 3, 4, 2]
k = Solution().findDuplicate(arr)
print(k)
        
# https://leetcode.com/problems/find-the-duplicate-number/
