from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR of a number with itself gives 0
        # XOR of a number with 0 give the number
        number = 0
        for i in nums:
            number = number ^ i
        return number



## 
        print(nums)
arr = [4, 1, 2, 1, 2]
k = Solution().singleNumber(arr)
print(k)
        
# https://leetcode.com/problems/single-number/
