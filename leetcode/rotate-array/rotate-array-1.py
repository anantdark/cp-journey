class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buffer = nums[len(nums)-k:]
        # using nums[:] to slice the list in place and not make a copy
        nums[:] = buffer + nums[:-k]
## 
        print(nums)
Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)
        
# https://leetcode.com/problems/rotate-array/
