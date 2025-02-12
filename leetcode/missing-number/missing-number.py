from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        return  (length*(length+1)//2) - sum(nums)


        
        
## 
        print(nums)
nums = [3, 0, 1]
k = Solution().missingNumber(nums)
print(k)
        
# https://leetcode.com/problems/missing-number/
