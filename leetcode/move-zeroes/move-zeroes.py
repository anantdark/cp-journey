from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a, b = 0, 0
        zero_count = nums.count(0)
        count = len(nums) - zero_count
        if not (count and zero_count):
            return
        while count:
            if nums[a] != 0:
                nums[b] = nums[a]
                b += 1
                a += 1
                count -= 1
            elif nums[a] == 0:
                a += 1
        nums[-zero_count:] = [0] * zero_count
        
## 
        print(nums)
nums = [1, 3, 4, 5, -2, 52, 0]
Solution().moveZeroes(nums)
        
# https://leetcode.com/problems/move-zeroes/
