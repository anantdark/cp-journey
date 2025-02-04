class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr_size = len(nums)
        k = k % arr_size
        # reverse both parts in place then reverse whole array
        # will use no extra space and will rotate in place
        nums[:arr_size-k] = nums[:arr_size-k][::-1]
        nums[arr_size-k:] = nums[arr_size-k:][::-1]
        nums[:] = nums[::-1] 
## 
        print(nums)
Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)
        
# https://leetcode.com/problems/rotate-array/
