from typing import List, Optional
from collections import defaultdict

# Naive solution
# Time O(n) | Space O(1)
# 

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mycounter = defaultdict(int)
        for val in nums:
            mycounter[val] += 1

        idx0 = mycounter[0]
        idx1 = mycounter[0] + mycounter[1]
        
        nums[:idx0] = [0]*mycounter[0]
        nums[idx0:idx1] = [1]*mycounter[1]
        nums[idx1:] = [2]*mycounter[2]

## 
        print(nums)
arr = [1, 2, 0, 1, 0, 2]
k = Solution().sortColors(arr)
print(k)
        
# https://leetcode.com/problems/sort-colors/
