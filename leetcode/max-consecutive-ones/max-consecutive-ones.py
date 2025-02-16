from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter, max_count = 0, 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                if max_count < counter:
                    max_count = counter
                counter = 0
            else:
                counter += 1
        return max(max_count, counter)
        

        
        
## 
        print(nums)
nums = [1, 1, 0, 1, 1, 1]
k = Solution().findMaxConsecutiveOnes(nums)
print(k)
        
# https://leetcode.com/problems/max-consecutive-ones/
