class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            temp = nums.pop(-1)
            nums.insert(0, temp)

        ##
        print(nums)
Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)
        
# https://leetcode.com/problems/rotate-array/
