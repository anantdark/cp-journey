class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr_size = len(nums)
        k = k % arr_size
        buffer = nums[arr_size-k:]
        # using nums[:] to slice the list in place and not make a copy
        nums[:] = buffer + nums[:arr_size-k]
## 
        print(nums)
Solution().rotate([1, 2], 5)
        
# https://leetcode.com/problems/rotate-array/
