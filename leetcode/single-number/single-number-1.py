from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        nums.append(nums[0]-1)
        nums.extend([nums[-1] - 1])
        for i in range(len(nums)):
            if nums[i] == nums[i+1] or nums[i] == nums[i-1]:
                continue
            else:
                return nums[i]

## 
        print(nums)
arr = [4, 1, 2, 1, 2]
k = Solution().singleNumber(arr)
print(k)
        
# https://leetcode.com/problems/single-number/
